from django.urls import path

from . import views


app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
]