from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        me = '/users/me/'
        if not request.user.is_authenticated:
            return False
        if me in request.path:
            return True
        if (request.user.username is not None
                and request.user.username in request.path):
            return True
        return request.user.is_admin
