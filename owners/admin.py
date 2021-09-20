from django.contrib import admin

from .models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('login', 'type',)
    search_fields = ('login',)
    list_filter = ('login',)
