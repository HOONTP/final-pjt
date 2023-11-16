# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# # Register your models here.

# admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'username', 'email', 'nickname', 'is_active', 'is_staff']

    fieldsets = (
        (None, {'fields': ('nickname','username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nickname', 'username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
    )

admin.site.register(CustomUser, UserAdmin)
