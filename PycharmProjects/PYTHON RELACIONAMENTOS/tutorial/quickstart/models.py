from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    nome_da_rua = models.CharField(max_length=60)
    numero_da_casa = models.IntegerField()
    complemento = models.CharField(max_length=60)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    cep = models.IntegerField()
    celular = models.CharField(max_length=11)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.id


class Procedimento(models.Model):
    data_procedimento = models.DateField(primary_key=True)
    numero_da_carteirinha = models.CharField(max_length=15)
    valor = models.DecimalField(decimal_places=13, max_digits=15)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'procedimento'

    def __str__(self):
        return self.data_procedimento