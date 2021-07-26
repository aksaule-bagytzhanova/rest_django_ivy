from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializer import ProductListSerializer


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