
from django.urls import path

from .views import ListProducts, ProductDetailView, ProductViewSet

from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('productviewset', ProductViewSet, basename='product')

urlpatterns = [
    path("productlist/", views.listproducts, name="ListProduct_view"),
    path("messagelist/", views.list_messages, name="message"),
    path("classproductlist/", ListProducts.as_view(), name="ListProducts"),
    path("classDetailedProduct/<int:pid>/", ProductDetailView.as_view(), name="DetailedProduct"),
    path("mixinpath/", views.ListProductsMixins.as_view(), name="mixinpath"),
    path("productmixin/<int:pk>/", views.DetailedProductMixins.as_view(), name="productmixin"),
    path("productgenericlist/",views.ListProductsGenerics.as_view(), name="productgenericlist"),
    path("productgenericdetail/<int:pk>/", views.DetailedProductsGenerics.as_view(), name="productgenericlist"),
    path("special/<int:pk>/", views.SpecialroductsGenerics.as_view(), name="spg"), 

]+router.urls


