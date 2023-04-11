from django.urls import path 
from . import views



app_name = 'posts'

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_post, name="submit"),
    path("profile/<int:user_name_id>", views.profile , name="profile"),

]
