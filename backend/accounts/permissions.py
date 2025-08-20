from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        u = request.user
        return bool(u and u.is_authenticated and getattr(u, "isAdmin", lambda : False)())

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        u = request.user
        if not (u and u.is_authenticated):
            return False

        return bool(getattr(u, "isAdmin", lambda : False)() or getattr(u, "isManager", lambda : True)())