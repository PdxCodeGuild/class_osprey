from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add, name='add_item'),
    path('<int:item_id>/complete/', views.complete, name='complete_item')
    # add delete item
]