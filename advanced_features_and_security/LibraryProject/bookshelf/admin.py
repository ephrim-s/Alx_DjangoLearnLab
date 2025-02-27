from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'groups']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissoins', {'fields':('is_active' 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )
    
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissoins', {'fields':('is_active' 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)