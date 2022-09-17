from django.db import models

from core.models import BaseModel


# Create your models here.
class Entry(BaseModel):

    tipo_pagamento = models.CharField(verbose_name="Tipo Pagamento", max_length=100) #Field.choices
    descrição = models.CharField(verbose_name="Descrição", max_length=255)
    valor = models.FloatField(verbose_name="Valor",max_length=10, default=0)
    paid_at =  models.DateTimeField(verbose_name="Pago em", auto_now=False, auto_now_add=False)
    banco = models.ForeignKey("bank_account.BankAccount", verbose_name="Banco", on_delete=models.CASCADE)
    entry_type = models.OneToOneField("entries.EntryType", verbose_name="Entry Type", on_delete=models.CASCADE)

    class Meta:
        verbose_name ="Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return f'{self.tipo_pagamento} - {self.descrição}'

class EntryType(BaseModel):

    nome =  models.CharField(verbose_name="Nome", max_length=50)

    class Meta:
        verbose_name = "Entry Type"
        verbose_name_plural = "Entry Types"

    def __str__(self):
        return self.nome
