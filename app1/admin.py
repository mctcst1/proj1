from django.contrib import admin
from . import models


@admin.register(models.Test)
class Teset(admin.ModelAdmin):
    pass
