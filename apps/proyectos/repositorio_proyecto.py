from apps.proyectos.models import ORMProyecto
from apps.proyectos.nombre_proyecto import NombreProyecto
from apps.proyectos.proyecto import Proyecto


class RepositorioProyecto(object):

    # def _decode_db(self, db_proyecto):
    #     proyecto = Proyecto(nombre=NombreProyecto(db_proyecto.nombre),
    #                         cliente=db_proyecto.cliente.id,
    #                         presupuesto=db_proyecto.presupuesto)
    #     return proyecto

    def create(self, proyecto):
        try:
            ORMProyecto.objects.create(nombre=proyecto.nombre.value,
                                       cliente_id=proyecto.cliente.id)
        except Exception as ex:
            raise ValueError(str(ex))
