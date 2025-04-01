from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombreEnpresa = models.CharField(max_length=200)