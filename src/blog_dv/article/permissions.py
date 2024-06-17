from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    '''
    权限
    '''

    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
