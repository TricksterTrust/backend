from rest_framework.permissions import BasePermission

from core.permission import DefaultPermission


class PromotionPermission(DefaultPermission):
    DANGER_METHODS = ["post", "patch", "delete", "put"]

