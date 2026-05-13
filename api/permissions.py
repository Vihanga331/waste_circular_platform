from rest_framework.permissions import BasePermission


class HasPlatformRole(BasePermission):
    """Future API RBAC gate for web, mobile, and AI service clients."""

    allowed_roles = ()

    def has_permission(self, request, view):
        roles = getattr(view, "allowed_roles", self.allowed_roles)
        return bool(request.user and request.user.is_authenticated and request.user.role in roles)
