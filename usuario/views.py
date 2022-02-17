from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Ola')

def login(request):
    return render(request, 'login.html')

def home(request):
    return HttpResponse('Você esta na pagina principal')