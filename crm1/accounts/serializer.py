from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


