from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('residence/',views.residence),
    path('index/',views.index),
    path('user/',views.user) 
    #path('', views.home, name='home_url_name'),
    #path('index/', views.index, name='index_url_name'),
    #path('user/', views.user, name='user_url_name')   
]