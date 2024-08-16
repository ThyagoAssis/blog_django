from django.db import models
from django import forms

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    conteudo = models.CharField(max_length=50, null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/', null=False)