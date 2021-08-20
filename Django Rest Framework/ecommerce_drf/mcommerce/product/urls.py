
from django.urls import path

from .views import ListProducts, ProductDetailView
from . import views



urlpatterns = [
    path("productlist/", views.listproducts, name="ListProduct_view"),
    path("messagelist/", views.list_messages, name="message"),
    path("classproductlist/", ListProducts.as_view(), name="ListProducts"),
    path("classDetailedProduct/<int:pid>/", ProductDetailView.as_view(), name="DetailedProduct"),

]


