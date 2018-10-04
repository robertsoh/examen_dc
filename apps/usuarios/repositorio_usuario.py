from apps.usuarios.models import ORMClienteUsuario


class RepositorioUsuario(object):

    def create(self, usuario):
        try:
            ORMClienteUsuario.objects.create(username=usuario.username.value,
                                             cliente_id=usuario.cliente.id,
                                             rol=usuario.rol.value)
        except Exception as ex:
            raise ValueError(str(ex))
