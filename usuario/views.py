from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def cadastro(request):
    return HttpResponse('Ola')

def login(request):
    return render(request, 'login.html')

def home(request):
    return HttpResponse( 'Você esta na pagina principal')

def salvar(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    idade = request.POST.get('idade')
    usuario = Usuario(
        nome = nome,
        sobrenome = sobrenome,
        idade = idade
    )
    usuario.save()
    return HttpResponse('Teste')

