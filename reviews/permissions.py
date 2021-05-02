from rest_framework.permissions import BasePermission


class IsAuthorized(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST']:
            return True
        if request.method in ['PATCH', 'DELETE']:
            return (request.user.is_admin_or_moderator
                    or obj.author == request.user)
