from django.db import models

class Bank_Account(models.model):
    nome = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10)
    tipo_conta = models.CharField(max_length=100) #Field.choices