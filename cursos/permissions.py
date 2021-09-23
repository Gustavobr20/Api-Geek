from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):
    # Verifica se o usuario é super usuario e deixa deletar caso contrario não.
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
