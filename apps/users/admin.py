from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import VerifyCode, UserProfile


class VerifyCodeAdmin(ModelAdmin):
    list_display = ['id', 'code', 'mobile', "add_time"]


class UserProfileAdmin(ModelAdmin):
    list_display = ['id', 'password', 'last_login', 'is_superuser',
                    'username', 'first_name', 'last_name', 'is_staff',
                    'is_active', 'date_joined', 'name',
                    'birthday', 'mobile', 'gender', 'email']


admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
