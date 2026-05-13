class RoleRequiredMixin:
    """Future RBAC mixin for Django class-based views."""

    allowed_roles = ()

    def has_role(self, user):
        return user.is_authenticated and user.role in self.allowed_roles
