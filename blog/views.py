from django.shortcuts import render
from . import models
from django.http import HttpResponse
import json

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_json_page(request,article_id):
    article = models.Article.objects.get(pk = article_id)
    response_data = {}
    response_data['title'] = article.title
    response_data['content'] = article.content
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def article_page(request,article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title','Title')
    content = request.POST.get('content','Content')
    article_id = request.POST.get('article_id','0')
    if article_id == 0:
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})

# Create your views here.
