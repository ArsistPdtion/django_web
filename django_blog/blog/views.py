from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def index(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list,10)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request,'index.html',locals())


def detail(request,page):
    article = Article.objects.get(id=page)
    return render(request,'detail.html',locals())

