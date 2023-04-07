from django.urls import path

from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('done/<int:item_id>/', views.done, name='done'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]

