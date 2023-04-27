from django.db import models
from rest_framework import serializers
from pokemon.models import Pokemon, Type






class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Type
        fields = ('id', 'type')



class PokemonSerializer(serializers.ModelSerializer):
    
    types = TypeSerializer(many= True)
    class Meta:
        model = Pokemon
        fields = ('types', 'number', 'name', 'height', 'weight',
                   'image_front', 'image_back', 'caught_by')