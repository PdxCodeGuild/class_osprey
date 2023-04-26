from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentAPIView.as_view()),
    path('new/', AddStudent.as_view()),
    path('<int:pk>/', StudentView.as_view()),
    path('<str:first_name>', StudentSearch.as_view()),
]