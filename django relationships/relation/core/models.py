from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

# one to one
class Phone(models.Model):    
    phone_no = models.CharField(max_length = 15)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="number")
    
    def __str__(self):
        return self.phone_no
    
    
    

# foreign key - one to many    
class Department(models.Model):
    name = models.CharField(max_length=15)    

    def __str__(self):
        return (f"{self.name}, {self.id}")


class Employee(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()    
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employeees_rel")

    def __str__(self):
        return self.name


# prefetch related

class Book(models.Model):
    book_name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)    
    
    def __str__(self):
        return self.book_name
    
    
class Store(models.Model):
    store_name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.store_name
    
    
