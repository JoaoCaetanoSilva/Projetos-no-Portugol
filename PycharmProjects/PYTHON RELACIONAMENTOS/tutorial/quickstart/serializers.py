from rest_framework import serializers
from .models import Paciente, Procedimento

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ProcedimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'