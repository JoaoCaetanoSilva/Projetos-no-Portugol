from rest_framework import serializers
from .pacientes_model import Paciente

class AposentadoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class DataDeNascimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['ano_de_nascimento']

class IdadeSerializer(serializers.Serializer):
    idade = serializers.IntegerField(required=False)
