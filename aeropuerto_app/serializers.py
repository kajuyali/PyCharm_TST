from rest_framework import serializers
from aeropuerto_app.models import *

# Crea los serializadores
class Avion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = ('__all__')

class Piloto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = ('__all__')

class Tripulacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tripulacion
        fields = ('__all__')

class Vuelo_Serializer(serializers.ModelSerializer):
    avion = Avion_Serializer(read_only=True)  # For GET trae el objeto
    avion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Avion.objects.all(), source='avion')  # For POST usa el id
    piloto = Piloto_Serializer(read_only=True)  # For GET trae el objeto
    piloto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Piloto.objects.all(), source='piloto')  # For POST usa el id
    class Meta:
        model = Vuelo
        fields = ('__all__')

class Itinerario_Serializer(serializers.ModelSerializer):
    vuelo = Vuelo_Serializer(read_only=True)  # For GET trae el objeto
    vuelo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vuelo.objects.all(), source='vuelo')  # For POST usa el id
    tripulacion = Tripulacion_Serializer(read_only=True)  # For GET trae el objeto
    tripulacion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tripulacion.objects.all(), source='tripulacion')  # For POST usa el id
    class Meta:
        model = Itinerario
        fields = ('__all__')
