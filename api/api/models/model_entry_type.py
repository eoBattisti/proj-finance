from django.db import models

class Entry_Type(models.model):
    nome = models.CharField(max_length= 100)
