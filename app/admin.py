from django.contrib import admin
from .models import Candidato, Empresa, Vaga, Candidatura, Chat, Conteudo, Autenticacao
from .models import Candidato, Empresa, Vaga, Candidatura, Chat, Conteudo, Autenticacao

admin.site.register(Candidato)
admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(Chat)
admin.site.register(Conteudo)
admin.site.register(Autenticacao)