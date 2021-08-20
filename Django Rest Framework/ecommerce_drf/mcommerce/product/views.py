
from django.shortcuts import render
from . models import Product
from . serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def listproducts(request):
    query = Product.objects.all()
    serializer_class = ProductSerializer(query, many=True)

    context = {
        "serializer_class_data": serializer_class.data ,
    }

    return Response(serializer_class.data)
