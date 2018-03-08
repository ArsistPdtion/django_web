from django.shortcuts import render
from .models import Article,Category,Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import markdown

# Create your views here.

#实现分页功能
def my_paginator(request,articles_list,page_num):
    paginator = Paginator(articles_list, page_num)
    page = request.GET.get('page', 1)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return article_list

def index(request):
    '''
    articles_list:所有的文章
    three_news_article:3篇最新的文章
    '''
    articles_list = Article.objects.all().order_by('-pub_date')
    #获取分页
    article_list = my_paginator(request,articles_list,5)

    #获取最新的三篇文章
    three_news_article = Article.objects.all().order_by('-pub_date')[:3]

    #获取分类数据
    category_dict = {}
    categoies = Category.objects.all()
    for category in categoies:
        category_dict[category] = Article.objects.filter(category=category).count()

    #获取标签数据
    tags = Tag.objects.all()

    #获取归档信息
    articles_time = Article.objects.all().values('pub_date')
    time_list = []
    for article_time in articles_time:
        time_list.append((article_time['pub_date'].year,article_time['pub_date'].month))
    time_set = set(time_list)

    return render(request,'index.html',locals())


def detail(request,page):
    article = Article.objects.get(id=page)
    article.increase_view_num()
    article.content = markdown.markdown(article.content,
                                        extensions = [
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    return render(request,'detail.html',locals())


def all_articles(request):
    articles_list = Article.objects.all().order_by('-pub_date')
    # 获取分页
    article_list = my_paginator(request,articles_list, 5)
    return render(request,'full-width.html',locals())


## 按照分类区分文章列表
def category_articles(request,category):
    articles_list = Article.objects.filter(category__name=category).order_by('-pub_date')
    article_list = my_paginator(request,articles_list, 5)
    return render(request, 'full-width.html', locals())



## 按照发布时间区分文章
def pub_date_articles(request,pub_year,pub_month):
    articles_list = Article.objects.filter(pub_date__year=pub_year,pub_date__month=pub_month).order_by('-pub_date')
    article_list = my_paginator(request,articles_list, 5)
    return render(request, 'full-width.html', locals())


