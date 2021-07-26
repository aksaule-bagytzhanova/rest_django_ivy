from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        field = '__all__'
