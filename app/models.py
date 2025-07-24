from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    curriculo = models.TextField()
    experiencias = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    setor = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_empresa


class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    requisitos = models.TextField()
    tags = models.CharField(max_length=255, help_text="Palavras-chave separadas por vírgula")

    def __str__(self):
        return f"{self.cargo} - {self.empresa.nome_empresa}"


class Candidatura(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_candidatura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.nome} -> {self.vaga.cargo}"


class Chat(models.Model):
    remetente = models.CharField(max_length=100)  # email ou id
    destinatario = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remetente} -> {self.destinatario}"


class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    categoria = models.CharField(max_length=100, help_text="Ex: currículo, entrevista, carreira")

    def __str__(self):
        return self.titulo


class Autenticacao(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.email
