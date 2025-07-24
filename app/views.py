from django.shortcuts import render
from django.views import View
from .models import Candidato, Empresa, Vaga, Candidatura, Conteudo, Chat

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class RegistroCandidatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registro_candidato.html')

    def post(self, request, *args, **kwargs):
        # Aqui seria feito o salvamento do formulário do candidato
        return render(request, 'registro_candidato.html')

class RegistroEmpresaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registro_empresa.html')

    def post(self, request, *args, **kwargs):
        # Salvamento de dados da empresa
        return render(request, 'registro_empresa.html')

class LoginLogoutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # Lógica de autenticação
        return render(request, 'login.html')

class PerfilCandidatoView(View):
    def get(self, request, *args, **kwargs):
        candidato = Candidato.objects.first()  # Exemplo fixo, substituir por request.user
        return render(request, 'perfil_candidato.html', {'candidato': candidato})

class PerfilEmpresaView(View):
    def get(self, request, *args, **kwargs):
        empresa = Empresa.objects.first()  # Exemplo fixo, substituir por request.user
        return render(request, 'perfil_empresa.html', {'empresa': empresa})

class VagasView(View):
    def get(self, request, *args, **kwargs):
        vagas = Vaga.objects.all()
        return render(request, 'vagas.html', {'vagas': vagas})

class CandidaturaView(View):
    def get(self, request, *args, **kwargs):
        candidaturas = Candidatura.objects.select_related('vaga', 'candidato').all()
        return render(request, 'candidaturas.html', {'candidaturas': candidaturas})

class ChatView(View):
    def get(self, request, *args, **kwargs):
        mensagens = Chat.objects.all()
        return render(request, 'chat.html', {'mensagens': mensagens})

class ConteudoView(View):
    def get(self, request, *args, **kwargs):
        conteudos = Conteudo.objects.all()
        return render(request, 'conteudos.html', {'conteudos': conteudos})