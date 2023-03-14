from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    ano_de_nascimento = models.DateField(blank=False)
    ano_de_contratacao = models.DateField(blank=False)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.id