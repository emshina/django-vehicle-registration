from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CarListing
admin.site.unregister(User)
# admin.site.unregister(CarListing)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2'),
        }),
    )

    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    
# @admin.register(CarListing)
class Carlistmodel(admin.ModelAdmin):
    list_display = ('user', 'make', 'price', 'image')
    list_filter = ['model']
    search_fields = ['model', 'make']
    
admin.site.register(CarListing,Carlistmodel)
    