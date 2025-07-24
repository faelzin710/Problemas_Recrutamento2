from django.shortcuts import render
from django.views import View
from app.models import *
from django.contrib.messages import constants
from django.contrib import messages

def indexView(request):
    return render(request, 'index.html')
def registroView(request):
    form =  Candidato.objects.all()
    return render(request, 'registro.html', {'form': form})
def validaRegistro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        curriculo = request.POST.get('curriculo')
        c = Candidato(nome=nome, email=email,senha=senha, curriculo=curriculo)
        c.save()
        messages.success(request, 'Cadastrado com sucesso')
        return render(request, 'registro.html')