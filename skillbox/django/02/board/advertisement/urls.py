from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name="advertisement_list"),
    path('advertisement1/', views.advertisement1, name="advertisement1"),
    path('advertisement2/', views.advertisement2, name="advertisement2"),
    path('advertisement3/', views.advertisement3, name="advertisement3"),
    path('advertisement4/', views.advertisement4, name="advertisement4"),
    path('advertisement5/', views.advertisement5, name="advertisement5"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('categories/', views.categories, name="categories"),
    path('regions/', views.regions, name="regions"),
    path('about1/', views.About1.as_view(), name="about1"),

]

