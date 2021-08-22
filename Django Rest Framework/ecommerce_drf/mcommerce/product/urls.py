
from django.urls import path

from .views import ListProducts, ProductDetailView, ListProductsMixins
from . import views



urlpatterns = [
    path("productlist/", views.listproducts, name="ListProduct_view"),
    path("messagelist/", views.list_messages, name="message"),
    path("classproductlist/", ListProducts.as_view(), name="ListProducts"),
    path("classDetailedProduct/<int:pid>/", ProductDetailView.as_view(), name="DetailedProduct"),
    path("mixinpath/", views.ListProductsMixins.as_view(), name="mixinpath"),
    path("productmixin/<int:pk>/", views.DetailedProductMixins.as_view(), name="productmixin"),
    
]


