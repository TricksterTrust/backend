from rest_framework.permissions import BasePermission

from core.permission import DefaultPermission


class PromotionPermission(DefaultPermission):
    DANGER_METHODS = ["post", "patch", "delete", "put"]

    def has_permission(self, request, view):
        if view.action in self.DANGER_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return True

