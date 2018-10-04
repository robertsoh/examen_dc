from django.db import models


class ORMProyecto(models.Model):

    nombre = models.CharField('Nombre', max_length=100)
    presupuesto = models.IntegerField('Presupuesto')
    cliente = models.ForeignKey('clientes.ORMCliente')
