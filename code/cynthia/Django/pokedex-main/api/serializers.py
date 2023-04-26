from django.db import models
from rest_framework import serializers
from pokemon.models import Pokemon




class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight',
                   'image_front', 'image_back', 'caught_by')
