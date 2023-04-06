from rest_framework import permissions


# Кастомные классы разрешений

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Только администратор, но читать могут все.
    """

    def has_permission(self, request, view):
        # настройка разрешений на уровне ВСЕГО ЗАПРОСА от клиента
        # SAFE_METHODS - GET, HEAD, OPTIONS, т.е. запросы чтения:
        if request.method in permissions.SAFE_METHODS:
            return True  # т.е. разрешено всем
        return bool(request.user and request.user.is_staff)  # для админа


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Только автор, но читать могут все.
    """

    def has_object_permission(self, request, view, obj):
        # настройка разрешений на уровне ОТДЕЛЬНОЙ ЗАПИСИ из БД
        if request.method in permissions.SAFE_METHODS:
            return True
        # True только, если в запросе user тот же, что и в записи из БД:
        return obj.user == request.user
