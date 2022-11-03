from django.db import models
from aluno.models import Aluno
from disciplina.models import Disciplina
# Create your models here.

class Aluno_disciplina(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=10)

    def __str__(self):
        return self.periodo