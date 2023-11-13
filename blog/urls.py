from django.urls import path
from .import views

urlpatterns=[
    #path("<int:month>", views.monthly_challenge_by_number),
    #path("<str:month>", views.monthly_challenge, name= "month-challenge"),

    path('home/',views.home),
    path('index/',views.index),
    path('residence/',views.residence),
    path('user/',views.user)  
]