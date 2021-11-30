from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Order
from .serializer import ProductListSerializer, OrderListSerializer
from .service import get_client_ip, PaginationProducts


class ProductListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductListSerializer
    pagination_class = PaginationProducts

    def get_queryset(self):
        products = Product.objects.all()
        return products


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.filter()
    serializer_class = ProductListSerializer


class CreateProduct(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
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

