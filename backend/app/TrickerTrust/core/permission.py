from rest_framework.permissions import BasePermission


class DefaultPermission(BasePermission):
    DANGER_METHODS = []

    def has_permission(self, request, view):
        if view.action in self.DANGER_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return True