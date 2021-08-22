
from django.shortcuts import render
from . models import Product
from . serializer import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . test import Message
from product import serializer
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listproducts(request):
    query = Product.objects.all()
    serializer_class = ProductSerializer(query, many=True)

    return Response(serializer_class.data)


@api_view(['GET', 'POST'])
def list_messages(request):
    message_obj = Message("oleg@ruchkin.ru", "hi hello this is content")
    serializer_class = MessageSerializer(message_obj)

    return Response(serializer_class.data)


class ListProducts(APIView):
    
    def get(self, request): 
        query = Product.objects.all()
        serializer_class = ProductSerializer(query, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_obj = ProductSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response({"Success": f"Product {product_saved.name} created successfully"})
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    def get(self, request, pid):
        query = Product.objects.filter(product_id = pid)
        serializer_class = ProductSerializer(query, many=True)
        return Response(serializer_class.data)


    def post(self, request, pid):
        serializer_obj = ProductSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response({"Success": f"Product {product_saved.name} created successfully"})
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pid):
        product_obj = Product.objects.get(product_id=pid)
        serializer_obj = ProductSerializer(product_obj, data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response({"Success": f"Product {product_saved.name} updated successfully"})
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pid):
        product_obj = Product.objects.filter(product_id=pid).delete()
        return Response(status=status.HTTP_200_OK)


class ListProductsMixins(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DetailedProductMixins(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin, 
                            mixins.CreateModelMixin, 
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView,):    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
