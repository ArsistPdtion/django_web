from django.shortcuts import render
from .models import Article,Category,Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def index(request):
    '''
    articles_list:所有的文章
    three_news_article:3篇最新的文章
    '''
    articles_list = Article.objects.all()
    #获取分页
    paginator = Paginator(articles_list,5)
    page = request.GET.get('page',1)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    #获取最新的三篇文章
    three_news_article = Article.objects.all().order_by('-pub_date')[:3]

    #获取分类数据
    category_dict = {}
    categoies = Category.objects.all()
    for category in categoies:
        category_dict[category] = Article.objects.filter(category=category).count()


    #获取标签数据
    tags = Tag.objects.all()

    return render(request,'index.html',locals())


def detail(request,page):
    article = Article.objects.get(id=page)
    return render(request,'detail.html',locals())


def all_articles(request):
    articles_list = Article.objects.all().order_by('-mod_date')
    # 获取分页
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page', 1)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request,'full-width.html',locals())




