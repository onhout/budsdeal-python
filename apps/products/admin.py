from django.contrib import admin

from .models import Item, Category, ItemImage


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


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
