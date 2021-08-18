from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.Serializer):
    models=Product
    fields="_all__"