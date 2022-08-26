from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets, status
# Create your views here.
# The views es donde se produce la lógica de la application
# Se compone de un ingreso de información y una salida de information

class Avion_view(viewsets.ModelViewSet):   # ModelViewSet para GET, POST, PUT, DELETE, etc
    queryset = Avion.objects.all()
    serializer_class = Avion_Serializer

class Piloto_view(viewsets.ModelViewSet):   # ModelViewSet para GET, POST, PUT, DELETE, etc
    queryset = Piloto.objects.all()
    serializer_class = Piloto_Serializer
