from django.db import models
from django import forms

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    conteudo = models.TextField(max_length=255, null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True, null=True)