from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("oleg", views.oleg, name="oleg"),
    path("<str:name>", views.greet, name="greet")
]
