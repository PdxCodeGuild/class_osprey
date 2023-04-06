from django.urls import path

from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('done/', views.done, name='done'),
]

