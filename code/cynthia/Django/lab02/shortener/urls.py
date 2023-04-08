from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_url, name='submit'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]

