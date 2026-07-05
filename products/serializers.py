from rest_framework import serializers
from .models import Flavour

class FlavourSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Flavour
        fields = ['id', 'name', 'price_per_kg', 'image', 'is_active']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None