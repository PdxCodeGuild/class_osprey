from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_url, name='submit'),
    # path('result/<int:user_submission_id>/', views.result, name='result'),
]