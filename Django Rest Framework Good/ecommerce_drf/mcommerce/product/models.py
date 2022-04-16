
from django.db import models



# Create your models here.

class ProductCategory(models.Model):
    category_name = models.CharField(max_length = 30)
    category_id = models.PositiveIntegerField()

    def __str__(self):
        return self.category_name

    

class Product(models.Model):    
    category_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="product_category")
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length = 50)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()  # auto_now=False, auto_now_add=False
    description = models.TextField()
    
    def __str__(self):
        return self.name

