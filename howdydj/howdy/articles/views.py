from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

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
    
    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {
        'article': a,
        'latest_comments_list': latest_comments_list,
    })


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))
