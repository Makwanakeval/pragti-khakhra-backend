from rest_framework import serializers
from .models import Order, OrderItem, DailyProduction

class OrderItemSerializer(serializers.ModelSerializer):
    flavour_name = serializers.CharField(source='flavour.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['flavour', 'flavour_name', 'quantity_kg', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['customer', 'is_free_delivery']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        request = self.context.get('request')
        order = Order.objects.create(customer=request.user, **validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        # Used by admin to update status only
        validated_data.pop('items', None)
        return super().update(instance, validated_data)


class DailyProductionSerializer(serializers.ModelSerializer):
    made_by_name = serializers.CharField(source='made_by.username', read_only=True)
    flavour_name = serializers.CharField(source='flavour.name', read_only=True)

    class Meta:
        model = DailyProduction
        fields = ['id', 'made_by', 'made_by_name', 'flavour', 'flavour_name', 'quantity_kg', 'date']
        read_only_fields = ['made_by', 'date']