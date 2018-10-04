

class Proyecto(object):

    def __init__(self, nombre, cliente, presupuesto=0, id=None):
        self.nombre = nombre
        self.cliente = cliente
        self.presupuesto = presupuesto
        self.id = id
