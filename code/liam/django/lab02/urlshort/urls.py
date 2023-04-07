from django.urls import path

from . import views


app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
    path('<str:short_url>/', views.refer, name='refer'),
]