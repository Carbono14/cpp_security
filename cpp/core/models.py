from django.db import models
from django.contrib.auth.models import Group

class Permiso(models.Model):
    objeto = models.CharField(max_length=50)
    leer = models.BooleanField(default=False)
    crear = models.BooleanField(default=False)
    editar = models.BooleanField(default=False)
    remover = models.BooleanField(default=False)

class Rol(models.Model):
    permisos = models.ManyToManyField(Permiso)
    grupos = models.ManyToManyField(Group)
