from django.db.models import fields
from .models import *
from rest_framework import serializers

class GuitarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitarra
        fields = '__all__'

class BajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bajo
        fields = '__all__'

class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = '__all__'

class PercusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percusion
        fields = '__all__'

class AmplificadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amplificador
        fields = '__all__'

class AccesorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesorio
        fields = '__all__'

class GuitaSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Ingrese id")
    marca=serializers.CharField(label="Ingrese Marca")
    tipo_cuerpo=serializers.CharField(label="Ingrese Modelo")
    tipo_guitarra=serializers.CharField(label="Ingrese Tipo Guitarra")
    valor=serializers.IntegerField(label="Ingrese Valor")
    descripcion=serializers.CharField(label="Ingrese Descripción")

