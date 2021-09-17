from django.contrib import admin

from .models import Licence


@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ('key', 'name',)
    search_fields = ('key', 'name',)
    list_filter = ('name',)
