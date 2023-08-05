from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={'article': 'article'})

# def index(request):
#     return render(request, 'article/index.html', context={
#         'article': 'article'})