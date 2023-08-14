from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib import messages
from django.views import View
from django_blog.article.models import Article
from .forms import ArticleForm

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[0:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article,})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья добавлена!')
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form,})


# class CommentArticleView(View):

#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm()
#         return render(request, 'comment.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 name = form.cleaned_data['content'],

#                 )
#             comment.save()




# def index(request, tags, article_id):
#     return render(request, 'article/index.html', context={
#         'tags': tags,
#         'article_id': article_id})