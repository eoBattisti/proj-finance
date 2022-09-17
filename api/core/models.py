from django.db import models

# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

    class Meta:
        verbose_name = "base"
        verbose_name_plural = "bases"
