from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Обеспечивает доступ администратору,
    всем остальным только безопасные методы.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin
        return request.method in permissions.SAFE_METHODS
