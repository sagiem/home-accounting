from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users import models

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ['email', 'username',]

admin.site.register(models.CustomUser, CustomUserAdmin)

@admin.register(models.RoleUsers)
class RoleUserAdmin(admin.ModelAdmin):
    list_display = ('role',)


