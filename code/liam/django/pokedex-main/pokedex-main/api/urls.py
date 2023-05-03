from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PokemonAPIView.as_view()),
    path('users/', UserView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('current/', views.current_user, name='current_user'),
]