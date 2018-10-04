from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api_v1.crear_cliente_proyecto_usuario_dto import CrearClienteProyectoUsuarioDto
from apps.clientes.cliente import Cliente
from apps.clientes.nombre_cliente import NombreCliente
from apps.clientes.repositorio_cliente import RepositorioCliente
from apps.common.decorators import serialize_exceptions
from apps.common.result import Result
from apps.proyectos.nombre_proyecto import NombreProyecto
from apps.proyectos.proyecto import Proyecto
from apps.proyectos.repositorio_proyecto import RepositorioProyecto


class ClienteCreateAPIView(APIView):

    def __init__(self, *args, **kwargs):
        self._repositorio_cliente = RepositorioCliente()
        self._repositorio_proyecto = RepositorioProyecto()
        super().__init__(*args, **kwargs)

    @serialize_exceptions
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        dto = CrearClienteProyectoUsuarioDto(
            NombreCliente=request.data.get('NombreCliente'),
            NombreProyecto=request.data.get('NombreProyecto'))
        nombre_cliente_o_error = NombreCliente.create(dto.NombreCliente)
        nombre_proyecto_o_error = NombreProyecto.create(dto.NombreProyecto)
        es_valido, errores = Result.combine([nombre_cliente_o_error, nombre_proyecto_o_error])
        if not es_valido:
            raise ValidationError(errores)
        cliente = Cliente(nombre=nombre_cliente_o_error.value)
        cliente = self._repositorio_cliente.create(cliente)
        proyecto = Proyecto(nombre=nombre_proyecto_o_error.value,
                            cliente=cliente)
        self._repositorio_proyecto.create(proyecto)
        return Response('OK', status=status.HTTP_201_CREATED)
