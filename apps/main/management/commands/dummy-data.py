import random

import names
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from model_mommy import mommy
from faker import Faker
from apps.products import models
from apps.user.models import Profile


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.clear()
        self.make_category()
        self.make_subcategory()
        self.make_users()
        self.make_products()

    def clear(self):
        models.Category.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()

    def make_category(self):
        categories = (
            'Flowers', 'Extracts', 'Edible', 'Product'
        )
        for category in categories:
            mommy.make(models.Category, name=category, slug=category.lower())

    def make_subcategory(self):
        subcategories = (
            'INDICA%s', 'SATIVA%s', 'HYBRID%s'
        )
        parent_models = models.Category.objects.filter(parent_category__isnull=True)
        for num in range(1, 10):
            for subcategory in subcategories:
                name = subcategory % random.randint(1, 100)
                mommy.make(models.Category, name=name, slug=name.lower(),
                           parent_category=models.Category.objects.get(name=parent_models[random.randint(0, 3)]))

    def make_users(self):
        for num in range(1, 100):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            email = slugify(first_name + '_' + last_name) + '@gmail.com'
            username = 'username' + str(num)
            mommy.make(
                User,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )

    def make_products(self):
        fake = Faker()
        category_model = models.Category.objects.filter(parent_category__isnull=False)
        for num1 in range(1, 100):
            name = 'PRODUCT_' + str(random.randint(1, 1000))
            mommy.make(
                models.Item,
                name=name,
                user=User.objects.get(username='username' + str(random.randint(1, 99))),
                type=random.choice(['Indica', 'Sativa', 'Hybrid']),
                price=random.randint(100, 1000),
                count=random.randint(1, 500),
                description=fake.text(),
                categories=category_model[random.randint(0, category_model.count()-1)]
            )
