from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Create a custom user admin class
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employer', 'is_candidate', 'is_staff')  # Fields to display
    list_filter = ('is_employer', 'is_candidate', 'is_staff')  # Filters in the admin panel
    search_fields = ('username', 'email')  # Fields to search by
    ordering = ('username',)  # Order the list by username

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_employer', 'is_candidate', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_employer', 'is_candidate'),
        }),
    )

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
