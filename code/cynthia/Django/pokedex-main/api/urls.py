from django.urls import path
from .views import *

urlpatterns = [
    path('', PokemonAPIView.as_view()),
    path('<int:pk>/', PokemonDetailView.as_view()),
    path('<str:name>/', PokemonSearch.as_view()),
]