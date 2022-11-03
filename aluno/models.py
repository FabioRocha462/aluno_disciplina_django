from django.db import models
from disciplina.models import Disciplina
# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cod = models.CharField(max_length=15)
    disciplinas = models.ManyToManyField(Disciplina, related_name='disciplina')


    def __str__(self):
        return self.nome
