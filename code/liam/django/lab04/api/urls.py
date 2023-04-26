from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentAPIView.as_view()),
    path('search/', StudentSearch.as_view()),
    path('new/', CreateStudent.as_view()),
    path('<int:pk>/<str:first_name>/', StudentDetail.as_view())
]