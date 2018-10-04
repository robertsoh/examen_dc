from apps.common.result import Result
from apps.common.value_object import ValueObject


class NombreUsuario(ValueObject):

    def __init__(self, value):
        value = value or ''
        if not value:
            raise ValueError('El nombre del usuario no puede ser nulo o vacío')
        if len(value) > 20:
            raise ValueError('El nombre del usuario es muy largo')

    @classmethod
    def create(cls, nombre):
        try:
            return Result.ok(cls(nombre))
        except Exception as ex:
            return Result.fail({'NombreUsuario':  [str(ex)]})
