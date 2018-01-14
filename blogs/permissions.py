from rest_framework.permissions import BasePermission

'''
Permisos para borrar, modificar o ver los detalles de una entrada
'''


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method == 'GET' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.user == request.user:
            return True
