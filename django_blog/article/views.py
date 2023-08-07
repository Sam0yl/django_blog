from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django_blog.article.models import Article

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[0:15]
        return render(request, 'articles/index.html', context={'articles': articles})


def index(request, tags, article_id):
    return render(request, 'article/index.html', context={
        'tags': tags,
        'article_id': article_id})