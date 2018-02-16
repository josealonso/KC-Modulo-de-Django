from rest_framework.permissions import BasePermission


class UsersPermission(BasePermission):

    # Ver detalles de un usuario, eliminarlo o modificar sus datos:
    # solo pueden hacerlo el administrador y el propio usuario

    def has_permission(self, request, view):
        from users.api import UserDetailAPI

        if request.user.is_authenticated and isinstance(view, UserDetailAPI):
            return True
        else:
            return request.method != "GET" or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # obj es el usuario solicitado
        return request.user == obj or request.user.is_superuser

