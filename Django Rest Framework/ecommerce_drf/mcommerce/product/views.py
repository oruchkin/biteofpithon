from django.shortcuts import render
from . models import Product
from . serializer import ProductSerializer

# Create your views here.

def listproducts(request):
    query=Product.objects.all()
    serializer_class=ProductSerializer(query, many=True)

    
