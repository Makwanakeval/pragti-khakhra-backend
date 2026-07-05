from django.contrib import admin
from .models import Order, OrderItem, DailyProduction

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'shop_name', 'mobile_number', 'delivery_city', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'delivery_city')
    search_fields = ('customer_name', 'shop_name', 'mobile_number')
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'

@admin.register(DailyProduction)
class DailyProductionAdmin(admin.ModelAdmin):
    list_display = ('made_by', 'flavour', 'quantity_kg', 'date')
    list_filter = ('date', 'flavour', 'made_by')