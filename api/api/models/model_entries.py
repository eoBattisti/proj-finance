from django.db import models

class Entries(models.model):
    tipo_pagamento = models.CharField(max_length=100) #Field.choices
    descrição = models.CharField
