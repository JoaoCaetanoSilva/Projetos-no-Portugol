from django.shortcuts import render
from .models import Procedimento
from .models import Paciente
from rest_framework import viewsets, permissions
from .serializers import ProcedimentoSerializer, PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer
