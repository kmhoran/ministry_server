from rest_framework import permissions


class HasOfficerAccess(permissions.BasePermission):
    """
    Determine if user has access to officer menu
    """

    def has_permission(self, request, view):
        
        user_permissions = []
        for p in request.user.get_all_permissions():
            user_permissions.append(p)

        permission_name = "pages.has_officer_access"
        
        return permission_name in user_permissions

    