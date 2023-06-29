from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Inventory)
admin.site.register(models.Order)
admin.site.register(models.Transaction)