from django.contrib.auth.models import AbstractUser
from django.db import models


class ORMClienteUsuario(AbstractUser):
    cliente = models.ForeignKey('clientes.ORMCliente')
    rol = models.IntegerField()
