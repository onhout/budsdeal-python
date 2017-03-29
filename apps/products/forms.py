from django.forms import ModelForm
from django.forms.models import inlineformset_factory, modelformset_factory

from .models import Item, Category, ItemImage, Feedback


class AddProductForm(ModelForm):
    class Meta:
        model = Item
        exclude = 'id', 'user', 'view_count'

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        # self.fields['categories'].widget = CheckboxSelectMultiple()
        self.fields['categories'].queryset = Category.objects.filter(parent_category__isnull=False)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*required'


class EditProductForm(ModelForm):
    class Meta:
        model = Item
        exclude = 'id', 'user', 'view_count'

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.filter(parent_category__isnull=False)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*required'


class ImageForm(ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']
        exclude = ['item']


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['to_user', 'from_user']


UpdateImageFormSet = inlineformset_factory(Item, ItemImage, form=ImageForm, max_num=3)
AddImageFormSet = modelformset_factory(ItemImage, form=ImageForm, extra=3, max_num=3)
