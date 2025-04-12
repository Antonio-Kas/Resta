from django.contrib import admin
from django.utils.html import format_html
from restasite.models import MenuItem, TextContent, Address
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

# Custom AdminSite
class RestaAdmin(admin.AdminSite):
    site_header = 'Resta Administration'
    site_title = 'Resta Admin Portal'
    index_title = 'Welcome to Resta Management Portal'
    
    # Custom templates
    index_template = 'admin/custom_index.html'
    login_template = 'admin/login.html'
    
    # Add extra context data to the admin site
    def each_context(self, request):
        context = super().each_context(request)
        context['extra_context'] = {
            'restaurant_name': 'Resta',
            'version': '1.0',
        }
        return context
    
    # Ensure CSRF cookie is set
    @method_decorator(ensure_csrf_cookie)
    def index(self, request, extra_context=None):
        return super().index(request, extra_context)
    
    # Ensure CSRF cookie is set for login view as well
    @method_decorator(ensure_csrf_cookie)
    def login(self, request, extra_context=None):
        return super().login(request, extra_context)

# Create an instance of the custom admin site
resta_admin_site = RestaAdmin(name='resta_admin')

# ModelAdmin classes
class TextContentAdmin(admin.ModelAdmin):
    list_display = ['key', 'description', 'content_preview']
    search_fields = ['key', 'content', 'description']
    list_per_page = 20
    
    # Customizing displayed fields
    readonly_fields = ['created_at'] if hasattr(TextContent, 'created_at') else []
    
    # Custom field for content preview
    @admin.display(description="Content Preview")
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    
    # Field grouping
    fieldsets = (
        ('Basic Information', {
            'fields': ('key', 'description'),
        }),
        ('Content', {
            'fields': ('content',),
            'classes': ('wide', 'extrapretty'),
        }),
    )
    
    # Adding custom actions
    actions = ['mark_as_reviewed']
    
    @admin.action(description="Mark selected content as reviewed")
    def mark_as_reviewed(self, request, queryset):
        # This would be implemented if there was a 'reviewed' field
        # queryset.update(reviewed=True)
        self.message_user(request, f"{queryset.count()} items marked as reviewed.")

class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'building', 'order', 'full_address']
    list_filter = ['city']
    list_editable = ['order']
    ordering = ['order', 'city']
    search_fields = ['city', 'street', 'building']
    
    # Add a virtual field to display the full address
    @admin.display(description="Full Address")
    def full_address(self, obj):
        return f"{obj.city}, {obj.street} {obj.building}"
    
    # Field grouping
    fieldsets = (
        ('Location', {
            'fields': ('city', 'street', 'building'),
        }),
        ('Display Options', {
            'fields': ('order',),
            'description': 'Configure how addresses are sorted',
        }),
    )

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'price', 'image_preview']
    list_filter = ['type']
    search_fields = ['title', 'description']
    list_editable = ['price']
    
    # Add a custom date hierarchy if it exists
    date_hierarchy = 'created_at' if hasattr(MenuItem, 'created_at') else None
    
    # Add a method to preview the image
    @admin.display(description="Image")
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    
    # Field grouping
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description'),
        }),
        ('Pricing and Type', {
            'fields': ('price', 'type'),
            'classes': ('collapse',),
        }),
        ('Image', {
            'fields': ('image',),
            'description': 'Upload a high-quality image',
        }),
    )
    
    # Custom empty value display
    empty_value_display = '-'
    
    # Custom actions for MenuItems
    actions = ['set_breakfast', 'set_lunch', 'set_dinner']
    
    @admin.action(description="Set selected items as Breakfast")
    def set_breakfast(self, request, queryset):
        queryset.update(type='BRK')
        self.message_user(request, f"{queryset.count()} items set as Breakfast.")
    
    @admin.action(description="Set selected items as Lunch")
    def set_lunch(self, request, queryset):
        queryset.update(type='LUN')
        self.message_user(request, f"{queryset.count()} items set as Lunch.")
    
    @admin.action(description="Set selected items as Dinner")
    def set_dinner(self, request, queryset):
        queryset.update(type='DIN')
        self.message_user(request, f"{queryset.count()} items set as Dinner.")

# Register models with the custom admin site
resta_admin_site.register(TextContent, TextContentAdmin)
resta_admin_site.register(Address, AddressAdmin)
resta_admin_site.register(MenuItem, MenuItemAdmin)

# Also register with the default admin site
admin.site.register(TextContent, TextContentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(MenuItem, MenuItemAdmin)