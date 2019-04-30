from django.contrib import admin
from . import models

# admin.site.register(models.Test, Optinal_class_for change_display) # or
@admin.register(models.Test)
class Teste(admin.ModelAdmin):
    list_display = ('name', 'degree')
    search_fields = ('name', 'degree')
    list_filter = ('name', 'degree')
    date_hierarchy = 'date'
    ordering = ('-degree', )