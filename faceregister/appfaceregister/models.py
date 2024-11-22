from django.db import models
import json

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    # foto = models.ImageField(upload_to='fotos/alunos/') #acho que aqui vai ter que mudar ou criar esse caminho

    def _str_(self):
        return f"{self.matricula} - {self.nome}"


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    # foto = models.ImageField(upload_to='fotos/professores/')

    def _str_(self):
        return f"{self.matricula} - {self.nome}"


class CodificacaoFacial(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='codificacao_facial')
    codificacao = models.TextField()

    def set_codificacao(self, encoding):
        self.codificacao = json.dumps(encoding.tolist())

    def get_codificacao(self):
        return json.loads(self.codificacao)


class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='presencas')
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])

    def _str_(self):
        return f"Presença de {self.aluno.nome} com {self.professor.nome} em {self.data} - {self.status}"