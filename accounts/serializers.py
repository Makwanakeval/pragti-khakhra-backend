from rest_framework import serializers
from .models import CustomUser

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'mobile_number', 'shop_name', 'city', 'address']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            mobile_number=validated_data['mobile_number'],
            shop_name=validated_data.get('shop_name', ''),
            city=validated_data.get('city', ''),
            address=validated_data.get('address', ''),
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'mobile_number', 'shop_name', 'city', 'address', 'is_staff']