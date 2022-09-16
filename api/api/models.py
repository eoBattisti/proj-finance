from django.db import models

class User(models.model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

class Contact(models.model):
    Celular = models.CharField(max_length=12)
    Email = models.EmailField(max_length=100)

class Bank_Account(models.model):
    nome = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10)
    tipo_conta = models.CharField(max_length=100) #Field.choices

class Entries(models.model):
    tipo_pagamento = models.CharField(max_length=100) #Field.choices
    descrição = models.CharField

class Entry_Type(models.model):
    nome = models.CharField(max_length= 100)



