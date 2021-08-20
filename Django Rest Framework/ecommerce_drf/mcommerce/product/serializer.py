from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Product

#model serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        #fields = ['product_id', "name"]

# no model serializer
class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


