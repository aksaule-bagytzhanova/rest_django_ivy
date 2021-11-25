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

class OrderListView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderListSerializer(order, many=False)
        return Response(serializer.data)


class CreateOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(status=201)
