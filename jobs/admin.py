from django.contrib import admin
from .models import Job, Application

# Optionally, you can create custom admin classes to manage how models are displayed in the admin panel
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'created_at')  # Fields to display in the list view
    search_fields = ['title', 'company']  # Fields to search by in the admin panel
    list_filter = ('location',)  # Add filter options by location

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'resume')  # Fields to display in the list view
    list_filter = ('status',)  # Add filter options by status
    search_fields = ['user__username', 'job__title']  # Add search functionality for user and job title

# Register the models
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
