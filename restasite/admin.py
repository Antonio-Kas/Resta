from django.contrib import admin

from restasite.models import MenuItem, TextContent, Address

@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    list_display = ['key', 'description']
    search_fields = ['key', 'content']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'building', 'order']
    ordering = ['order']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'price']
    list_filter = ['type']