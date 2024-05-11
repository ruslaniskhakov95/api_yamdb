from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return (obj.author == request.user
                or request.user.is_admin or request.user.is_staff)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Обеспечивает доступ администратору,
    всем остальным только безопасные методы.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin
        return request.method in permissions.SAFE_METHODS
