from django.contrib import admin
from .models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
