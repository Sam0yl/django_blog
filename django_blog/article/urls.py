from django.urls import path

from django_blog.article.views import IndexView, ArticleFormCreateView, ArticleFormEditView, ArticleView


urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]