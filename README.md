# Resta Restaurant Management System

## Custom Admin Implementation

This project includes a customized Django admin interface that enhances the management of restaurant content:

### Features:

1. **Custom AdminSite**
   - Custom branding (title, header, welcome message)
   - Custom index page with restaurant-specific information
   - Available at `/resta-admin/` URL

2. **Enhanced ModelAdmin Classes**
   - **MenuItemAdmin**:
     - Custom image preview in list view
     - Fieldsets for organized form display
     - Actions for quickly changing item types (breakfast/lunch/dinner)
     - Editable price directly from list view
   
   - **AddressAdmin**:
     - List filtering by city
     - Inline ordering capability
     - Customized display of full address
   
   - **TextContentAdmin**:
     - Content preview in list view
     - Organized fieldsets
     - Custom actions for content management

### How to Access:

1. **Default Django Admin**: `/admin/`
2. **Custom Resta Admin**: `/resta-admin/`

### Implementation Details:

The custom admin implementation follows Django's best practices for extending the admin interface:

- Custom `AdminSite` class in `restasite/admin.py`
- Enhanced `ModelAdmin` classes with:
  - Custom actions
  - Display decorators
  - Fieldsets
  - List display customizations
  - Format HTML for image display
- Custom admin templates in `restasite/templates/admin/`

### Usage:

1. Run the development server: `python manage.py runserver`
2. Visit `/resta-admin/` in your browser
3. Log in with your admin credentials
4. Enjoy the enhanced management experience!

## Technical Notes

- Django 3.2+ is required
- Proper media settings are needed for image previews to work
- Template customization follows Django's template inheritance patterns 