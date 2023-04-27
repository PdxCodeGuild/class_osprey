from rest_framework import generics
from pokemon.models import Pokemon, Type
from users.models import CustomUser
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class PokemonAPIView(generics.ListAPIView):
    permission_class = permissions.IsAuthenticated
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class UserView(generics.ListAPIView):
    permission_class = permissions.IsAuthenticated
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = permissions.IsAuthenticated
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)