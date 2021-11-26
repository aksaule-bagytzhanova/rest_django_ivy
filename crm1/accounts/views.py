from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Order
from .serializer import ProductListSerializer, OrderListSerializer
from .service import get_client_ip


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        products = Product.objects.all()
        return products


class ProductDetailView(generics.RetrieveAPIView):

    queryset = Product.objects.filter()
    serializer_class = ProductListSerializer


class CreateProduct(generics.CreateAPIView):

    serializer_class = ProductListSerializer()

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class OrderListView(generics.ListAPIView):

    serializer_class = OrderListSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        return orders


class OrderDetailView(APIView):


    queryset = Order.objects.filter()
    serializer_class = OrderListSerializer



class CreateOrder(APIView):

    serializer_class = OrderListSerializer()

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

