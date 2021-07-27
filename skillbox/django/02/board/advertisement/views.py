from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View

# Create your views here.


class About1(View):
    def get(self, request):
        return render(request, "advertisement/about1.html",{

        }) 

    def post(self, reuest):
        return HttpResponse('')


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        "первое",
        "второе",
        "третье",
    ]
    return render(request, "advertisement/advertisement_list.html",
    {
        "advertisements": advertisements
    })


def regions(request):

    regions = ["Москва", "Московская область", "республика Алтай", "Вологодская область", "и т.д."]
    return render(request,"advertisement/regions.html",{
        "regions": regions,
    })

def categories(request):

    categories = ["личные вещи", "транспорт", "хобби и отдых"]

    return render(request, "advertisement/categories.html",{
        "categories": categories
    })

def about(request):
    nazvanie = "Бесплатные объявления"
    opisanie = "Бесплатные объявления в вашем городе!"

    return render(request, "advertisement/about.html", {
        "nazvanie": nazvanie,
        "opisanie": opisanie,
    })



def contacts(request):

    telephon = "8-800-708-19-45"
    e_mail = "sales@company.com"

    return render(request, "advertisement/contacts.html", {
        "telephon" : telephon,
        "e_mail" : e_mail,
    })



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
