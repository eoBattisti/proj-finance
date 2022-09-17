from django.db import models

from core.models import BaseModel

# Create your models here.
class User(BaseModel):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contact(BaseModel):
    celular = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.email} | {self.contact}'