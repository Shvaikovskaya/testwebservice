from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('login', 'description',)
    search_fields = ('login',)
    list_filter = ('login',)
