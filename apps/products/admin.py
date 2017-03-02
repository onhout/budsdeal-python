from django.contrib import admin

from .models import Item, Category


# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = [
        'user',
        'name',
        'type',
        'brand',
        'price',
    ]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [
        'name',
        'slug',
        'parent_category',
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
