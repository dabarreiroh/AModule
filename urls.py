from django.urls import path,re_path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    #path('<path:urls>',views.query, name='query'),
    re_path(r'^query/$', views.query,name='query'),
    #path(regex=r'^query/$', view='views.query',name='query'),
]