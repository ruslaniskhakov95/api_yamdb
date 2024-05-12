from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Доступ для авторов, модераторов и админов."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)


class IsModeratorOrAdminOrSuperUser(permissions.BasePermission):
    """Доступ для админа, модератора или суперюзера."""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.user.is_admin
                    or request.user.is_superuser
                    or request.user.is_moderator)


class IsAdmin(permissions.BasePermission):
    """Доступ для админа или суперюзера."""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Обеспечивает доступ администратору,
    всем остальным только безопасные методы.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin
        return request.method in permissions.SAFE_METHODS
