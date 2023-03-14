from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .serializers import AposentadoriaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .pacientes_model import Paciente
from .serializers import AposentadoriaSerializer, DataDeNascimentoSerializer, IdadeSerializer
from datetime import date

@csrf_exempt
def aposentadoria_list(request):
    if request.method == 'GET':
        snippets = Paciente.objects.all()
        resultado = AposentadoriaSerializer(snippets, many=True)
        return JsonResponse(resultado.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        resultado = AposentadoriaSerializer(data=data)
        if resultado.is_valid():
            resultado.save()
            return JsonResponse(resultado.data, status=201)
        return JsonResponse(resultado.errors, status=400)


@csrf_exempt
def aposentadoria_detail(request, id):
    try:
        aposentadoria = Paciente.objects.get(id=id)
    except Paciente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        data_do_dia = date.today()
        # data_nascimento = date(aposentadoria.ano_de_nascimento.year,
        #                        aposentadoria.ano_de_nascimento.month,
        #                        aposentadoria.ano_de_nascimento.day)

        idade = int((aposentadoria.ano_de_contratacao - aposentadoria.ano_de_nascimento).days / 365)
        data = {'idade':idade}
        resultado = IdadeSerializer(data=data)
        resultado.is_valid()
        return JsonResponse(resultado.data, status=200)



