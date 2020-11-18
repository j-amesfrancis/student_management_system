from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User


# Register your models here.

class AdminUser(UserAdmin):
    fieldsets = [
        ['User Info', {'fields': ['username', 'password']}],
        ['Personal Info', {'fields': ['email', 'first_name', 'last_name']}],
        ['User Status', {'fields': ['is_active', 'is_staff', 'is_superuser']}],
        ['User Roles', {'fields': ['user_roles']}],
        ['Important Dated', {'fields': ['last_login', 'date_joined']}],
    ]
    list_filter = ['is_staff', 'is_superuser', 'user_roles']


admin.site.register(User, AdminUser)
admin.site.unregister(Group)
