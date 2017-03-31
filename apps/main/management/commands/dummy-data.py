import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from model_mommy import mommy

from apps.products import models
from apps.user.models import Profile, Company

fake = Faker()


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        print('Clearing data...')
        self.clear()
        print('making categories...')
        self.make_category()
        print('making subcategories...')
        self.make_subcategory()
        print('making users...')
        self.make_users()
        print('making products...')
        self.make_products()
        print('making SLOW ASS product feedbacks...')
        self.make_product_feedback()
        print('DONE!')

    def clear(self):
        models.Category.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()
        models.Item.objects.all().delete()
        Company.objects.all().delete()

    def make_category(self):
        categories = (
            'Flowers', 'Extracts', 'Edibles', 'Products'
        )
        for category in categories:
            mommy.make(models.Category, name=category, slug=category.lower())

    def make_subcategory(self):
        parent_models = models.Category.objects.filter(parent_category__isnull=True)
        for num in range(1, 30):
            name = fake.catch_phrase().title()
            mommy.make(models.Category, name=name, slug=slugify(name),
                       parent_category=models.Category.objects.get(name=parent_models[random.randint(0, 3)]))

    def make_users(self):
        for num in range(1, 100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            username = 'username' + str(num)
            social_id = fake.uuid4()[:6]
            mommy.make(
                User,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )
            profile = Profile.objects.get(user=User.objects.get(username=username).id)
            profile.social_id = social_id
            profile.display_name = first_name.lower() + social_id
            profile.gender = random.choice(['Male', 'Female'])
            profile.approved_as_seller = random.choice([True, False])
            company = Company.objects.get(user=User.objects.get(username=username).id)
            company.name = fake.company()
            company.address = fake.address()
            company.address2 = fake.secondary_address()
            company.city = fake.city()
            company.state = fake.state_abbr()
            company.zip = fake.zipcode()
            company.phone_number = fake.phone_number()
            company.TIN = fake.random_number(20)

            profile.save()
            company.save()

    def make_products(self):
        category_model = models.Category.objects.filter(parent_category__isnull=False)
        for num1 in range(1, 1000):
            mommy.make(
                models.Item,
                name=fake.bs().title(),
                user=User.objects.get(username='username' + str(random.randint(1, 99))),
                brand=fake.company(),
                type=random.choice(['indica', 'sativa', 'hybrid']),
                price=fake.random_int(10, 10000),
                count=fake.random_int(1, 500),
                view_count=fake.random_number(4),
                description=fake.text(),
                categories=category_model[random.randint(0, category_model.count() - 1)]
            )

    def make_product_feedback(self):
        for num in range(1, 10000):
            mommy.make(
                models.Feedback,
                from_user=User.objects.get(username='username' + str(fake.random_int(1, 99))),
                to_item=models.Item.objects.order_by('?').first(),  # THIS IS GONNA BE SLOW
                item_rating=fake.random_int(1, 5),
                content=fake.text()
            )
