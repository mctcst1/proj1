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
    fields = ('name', 'degree', 'date')


@admin.register(models.Id)
class Ids(admin.ModelAdmin):
    pass


@admin.register(models.Book)
class Books(admin.ModelAdmin):
    filter_horizontal = ('author', )
    raw_id_fields = ('author', )


@admin.register(models.Gene)
class Genes(admin.ModelAdmin):
    pass