from django.urls import path
from .import views

urlpatterns = [
    #path("<int:month>", views.monthly_challenge_by_number),
    #path("<str:month>", views.monthly_challenge, name= "month-challenge"),

    path("",views.starting_page, name="starting-page"),
    path("posts",views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail-page")
   
]