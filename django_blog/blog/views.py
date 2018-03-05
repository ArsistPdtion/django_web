from django.shortcuts import render,get_object_or_404
from .models import Article

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    # return render(request,'base.html',context={'article_list':articles})
    return render(request,'index.html',locals())


def detail(request,page):
    article_id = get_object_or_404(Article,page_id=page)
    return render(request,'detail.html',locals())

