from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404

from .models import Article, Comment

# Create your views here.

def index(request):
    latest_aritcles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, "articles/list.html", {
        'latest_aritcles_list': latest_aritcles_list
    })


def test(request):
    pass

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {
        'article': a
    })

