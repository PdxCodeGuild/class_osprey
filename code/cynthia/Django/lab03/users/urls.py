from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path("users/", views.users, name="users"),
]

#url nmes must be unique