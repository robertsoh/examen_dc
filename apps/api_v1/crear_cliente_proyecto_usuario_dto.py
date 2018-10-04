from typing import NamedTuple


class CrearClienteProyectoUsuarioDto(NamedTuple):
    NombreCliente: str
    NombreProyecto: str

    def serialize(self):
        return self._asdict()
