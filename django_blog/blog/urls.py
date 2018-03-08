from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^article/(?P<page>[0-9]+)/$',views.detail,name='detail'),
    url(r'^all_articles/$',views.all_articles,name='all_article'),
    url(r'^category_articles/(?P<category>[\w]+)/$',views.category_articles,name='category_articles'),
    url(r'^article_date/(?P<pub_year>[1-9]+\d{3})/(?P<pub_month>[1-9]|1[0-2])/$',views.pub_date_articles,name='pub_date_articles'),

]

