from django.contrib import admin
from .models import Flavour

@admin.register(Flavour)
class FlavourAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg', 'is_active')