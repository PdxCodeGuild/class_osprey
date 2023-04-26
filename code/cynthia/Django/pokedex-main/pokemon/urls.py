from django.urls import path
from .views import PokemonListView

urlPatterns = [
    path('', PokemonListView.as_view(), name='pokemon')
]