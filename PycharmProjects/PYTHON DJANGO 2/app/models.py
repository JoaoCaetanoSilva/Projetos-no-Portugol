from django.shortcuts import render, redirect
from .pacientes_model import Paciente

def metodo_get(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['paciente'] = Paciente.objects.get(id=id_evento)
    # return render(request, 'evento.html', dados)

def metodo_post(request):
    nome = request.POST.get('nome')
    ano_de_nascimento = request.POST.get('ano_de_nascimento')
    ano_de_contratacao = request.POST.get('ano_de_contratacao')
    id_evento = request.POST.get('id_evento')
    if id_evento:
        Paciente.objects.create(nome=nome,
                                ano_de_nascimento=ano_de_nascimento,
                                ano_de_contratacao=ano_de_contratacao
                                )

def metodo_put(request):
    nome = request.POST.get('nome')
    ano_de_nascimento = request.POST.get('ano_de_nascimento')
    ano_de_contratacao = request.POST.get('ano_de_contratacao')
    id_evento = request.POST.get('id_evento')
    if id_evento:
        Paciente.objects.filter(id=id_evento).update(nome=nome,
                                                     ano_de_nascimento=ano_de_nascimento,
                                                     ano_de_contratacao=ano_de_contratacao)

def metodo_delete(request, id_evento):
    evento = Paciente.objects.get(id=id_evento)
    evento.delete()  # Faz apenas o usuario deletar seu evento.
    return redirect('/')