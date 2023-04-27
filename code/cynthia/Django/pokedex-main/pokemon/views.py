from django.shortcuts import render

from django.views.generic import ListView
from .models import Pokemon, Type



class PokemonListView(ListView):
    model = Pokemon
    template_name = 'home.html'
