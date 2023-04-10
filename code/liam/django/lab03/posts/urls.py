from django.urls import path

from . import views


app_name = 'posts'
urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.make_post, name="post"),
    path("user/<str:username>/", views.profile_view, name="profile"),
]