from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name= 'article_page'),
    url(r'^article_json/(?P<article_id>[0-9]+)$', views.article_json_page,name= 'article_json_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    url(r'^edit/aciton$', views.edit_action, name='edit_action'),
]
