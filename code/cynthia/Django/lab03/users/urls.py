from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path("", views.index, name="users"),
]

#url nmes must be unique