from django.shortcuts import render  #render is already imported in this new app
from .models import Article
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    # Below 'articles' refer to "Article.objects.all().order_by('date')"
    # Dictionary below is used to pull down the data to the html template.
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request):
    return HttpResponse(slug)
