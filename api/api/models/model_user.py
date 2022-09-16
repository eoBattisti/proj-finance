from django.db import models

class User(models.model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)