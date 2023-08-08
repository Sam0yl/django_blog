from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django_blog.article.models import Article

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[0:15]
        return render(request, 'articles/index.html', context={'articles': articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article,})


# def index(request, tags, article_id):
#     return render(request, 'article/index.html', context={
#         'tags': tags,
#         'article_id': article_id})