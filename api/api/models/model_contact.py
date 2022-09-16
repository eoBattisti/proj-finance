from django.db import models

class Contact(models.model):
    Celular = models.CharField(max_length=12)
    Email = models.EmailField(max_length=100)