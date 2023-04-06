from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add, name='add'),
    path('<int:item_id>/complete/', views.complete, name='complete'),
    path('<int:item_id>/remove/', views.remove, name='remove')
]