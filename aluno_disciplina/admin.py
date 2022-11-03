from django.contrib import admin
from aluno_disciplina.models import Aluno_disciplina
# Register your models here.

class Admin_Aluno_disciplina(admin.ModelAdmin):
    list_display = ['aluno','disciplina']
    search_fields = ('data_matricula',)

    
admin.site.register(Aluno_disciplina,Admin_Aluno_disciplina)