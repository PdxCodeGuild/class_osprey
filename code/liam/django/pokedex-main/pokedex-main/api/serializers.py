from rest_framework import serializers
from pokemon.models import Pokemon, Type
from users.models import CustomUser

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']

class PokemonSerializer(serializers.ModelSerializer):
    
    types = TypeSerializer(
        many=True,
        read_only=True,
    )
    
    class Meta:
        model = Pokemon
        fields = ['id', 'number', 'name', 'height', 'weight',
                  'image_front', 'image_back', 'caught_by',
                  'types']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'id', 'caught']