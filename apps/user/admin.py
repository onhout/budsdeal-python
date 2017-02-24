from django.contrib import admin

from .models import Profile, Company


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = [
        'user',
        'name',
        'address',
        'phone_number',
        'city',
        'state',
        'zip',
    ]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [
        'user',
        'gender',
        'social_id',
        'login_type',
    ]

admin.site.register(Company, CompanyAdmin)

admin.site.register(Profile, ProfileAdmin)
