from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        "первое",
        "второе",
        "третье",
    ]


    return render(request, "advertisement/advertisement_list.html")


def advertisement1(request):
    return render(request, "advertisement/advertisement1.html")


def advertisement2(request):
    return render(request, "advertisement/advertisement2.html")


def advertisement3(request):
    return render(request, "advertisement/advertisement3.html")


def advertisement4(request):
    return render(request, "advertisement/advertisement4.html")


def advertisement5(request):
    return render(request, "advertisement/advertisement5.html")
