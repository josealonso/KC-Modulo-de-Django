from rest_framework.permissions import BasePermission


class UsersPermission(BasePermission):

    # Ver detalles de un usuario, eliminarlo o modificar sus datos:
    # solo pueden hacerlo el administrador y el propio usuario

    def has_permission(self, request, view):
        from users.api import UserDetailAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailAPI):
            return True

        if request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE"):
            return True

        '''
        if not POST and not is_superuser:
            return False
        '''

    def has_object_permission(self, request, view, obj):
        # obj es el usuario solicitado
        return request.user == obj or request.user.is_superuser
