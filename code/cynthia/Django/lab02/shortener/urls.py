from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_url, name='submit'),
    path('new_url/<int:user_submission_id>/', views.new_url, name='new_url'),
]