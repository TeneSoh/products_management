from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer
from products.serializers import ProductSerializer
from users.permissions import Can_create_products, Can_view_allProducts, Can_view_product

# class ProductViewClass(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serialize = ProductSerializer(products, many=True)

#         return Response(serialize.data)
    
#     def post(self, request):
#         product = ProductSerializer(data = request.data)
#         print(product)
#         if product.is_valid():
#             product.save()

#             return Response(product.data, status=status.HTTP_201_CREATED)
        
#         return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ProductId(APIView):
#    #permission_classes = [IsAuthenticated, Can_create_products, Can_view_allProducts, Can_view_product]
#     def get(self,request, pk):
#         product = Product.objects.filter(pk = pk).first()
#         # faite la verification
#         serializer = ProductSerializer(product)

#         return Response(serializer.data)
    

class ProductViewClass(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]