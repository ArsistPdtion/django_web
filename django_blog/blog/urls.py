from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^article/?P<id>[0-9]+/$',views.detail,name='detail'),
]

