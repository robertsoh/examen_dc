from typing import NamedTuple


class CrearClienteProyectoUsuarioDto(NamedTuple):
    NombreCliente: str
    NombreProyecto: str
    NombreUsuario: str
    Rol: int = None

    def serialize(self):
        return self._asdict()
