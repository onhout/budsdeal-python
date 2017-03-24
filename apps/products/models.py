import os
from uuid import uuid4

import django.db.models.options as options
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

es_client = settings.ES_CLIENT

options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent_category = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    TYPE = [
        ('indica', 'Indica'),
        ('sativa', 'Sativa'),
        ('hybrid', 'Hybrid'),
    ]
    WEIGHT_UNIT = [
        ('g', 'g'),
        ('kg', 'kg'),
        ('oz', 'oz'),
        ('lb', 'lb'),
        ('unit', 'unit'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=10, choices=TYPE)
    brand = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.IntegerField()
    weight_unit = models.CharField(max_length=10, choices=WEIGHT_UNIT)
    categories = models.ForeignKey(Category, related_name='categories')
    description = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        es_index_name = 'django'
        es_type_name = 'item'
        es_mapping = {
            'properties': {
                'name': {'type': 'string'},
                'brand': {'type': 'string'},
                'type': {'type': 'string', 'index': 'not_analyzed'},
                'description': {'type': 'string'},
                'categories': {
                    'type': 'object',
                    'properties': {
                        "name": {'type': 'string'},
                        "slug": {'type': 'string'}
                    }
                }
            }
        }

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {}
                field_es_value['_id'] = related_object.pk
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value

    def get_es_name_complete(self):
        return {
            "input": [self.name],
            "output": "%s %s" % self.name,
            "payload": {"pk": self.pk},
        }

    def get_es_item_names(self):
        if not self.item.exists():
            return []
        return [c.name for c in self.item.all()]

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(Item, self).save(*args, **kwargs)
        payload = self.es_repr()
        if is_new:
            del payload['_id']  # ITS ONLY CUZ OF THIS! CAUSING THE DOC ADDED!
            es_client.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body=payload  # CHANGED HOW THE PAYLOAD IS LOADED!!!
            )
        else:
            del payload['_id']
            es_client.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Item, self).delete(*args, **kwargs)
        es_client.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )


def get_file_path(instance, filename):
    filename = '%s.%s' % (uuid4(), 'jpg')
    return os.path.join(instance.directory_string, filename)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=get_file_path,
                                processors=[ResizeToFill(640, 480)],
                                format='JPEG',
                                options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    directory_string = './static/media/item_pics'


@receiver(post_delete, sender=ItemImage)
def image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


@receiver(pre_save, sender=ItemImage)
def image_update(sender, instance, **kwargs):
    try:
        old_item = ItemImage.objects.get(pk=instance.id)
        if old_item.image:
            old_item.image.delete(False)
    except ItemImage.DoesNotExist:
        pass
