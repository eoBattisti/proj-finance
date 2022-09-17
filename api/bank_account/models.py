from django.db import models
from core.models import BaseModel

# Create your models here.
class BankAccount(BaseModel):
    nome = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    saldo = models.FloatField()
    tipo_conta = models.CharField(max_length=100)
    dono = models.ForeignKey("users.User", verbose_name="User", on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"

    def __str__(self):
        return self.nome
