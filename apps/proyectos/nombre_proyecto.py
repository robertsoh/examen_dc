from apps.common.result import Result
from apps.common.value_object import ValueObject


class NombreProyecto(ValueObject):

    def __init__(self, value):
        value = value or ''
        if not value:
            raise ValueError('El nombre del proyecto no puede ser nulo o vacío')
        if len(value) > 100:
            raise ValueError('El nombre del proyecto es muy largo')

    @classmethod
    def create(cls, nombre):
        try:
            return Result.ok(cls(nombre))
        except Exception as ex:
            return Result.fail({'name':  [str(ex)]})
