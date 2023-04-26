from django.shortcuts import render
from rest_framework import generics
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonAPIView(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()
    
class PokemonDetailView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonSearch(generics.ListAPIView):
    serializer_class = PokemonSerializer
    def get_queryset(self):
        pokemon_name = self.kwargs['name']
        return Pokemon.objects.filter(name = pokemon_name)