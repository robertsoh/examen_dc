from enum import Enum


class RolUsuario(Enum):
    Owner = 1
    Supervisor = 2
    Assistant = 3


class Usuario(object):

    def __init__(self, username, cliente, rol, id=None):
        self.username = username
        self.cliente = cliente
        self.rol = rol
        self.id = id
