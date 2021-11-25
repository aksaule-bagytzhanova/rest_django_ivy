from rest_framework import serializers
from .models import Product, Order


class ProductListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field="name", read_only=True)
    product = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'







