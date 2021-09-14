from django.contrib import admin

# Register your models here.
from .models import Phone, Department, Employee, Store, Book

admin.site.register(Phone)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Store)
admin.site.register(Book)

