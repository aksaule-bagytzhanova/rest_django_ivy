from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Order
from .serializer import ProductListSerializer, OrderListSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductListSerializer(product, many=False)     
        return Response(serializer.data)


class CreateProduct(APIView):

    def post(self, request, format=None):
        serializer = ProductListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()


class OrderListView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderListSerializer(order, many=True)
        return Response(serializer.data)


class CreateOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
