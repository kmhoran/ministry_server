from rest_framework import permissions


class CanSeePenguins(permissions.BasePermission):
    """
    Custom permission to restrict accesss to penguins
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
            # return True

        # Write permissions are only allowed to the owner of the snippet.
        user_permissions = []
        for p in request.user.get_all_permissions():
            user_permissions.append(p)

        view_permission = "main.can_see_penguins"
        return view_permission in user_permissions


class CanViewMemberMenu(permissions.BasePermission):
    """
    Determine if user has access to member menu
    """

    def has_permission(self, request, view):
        
        user_permissions = []
        for p in request.user.get_all_permissions():
            user_permissions.append(p)

        view_permission = "main.can_access_member_menu"
        return view_permission in user_permissions


class CanViewOfficerMenu(permissions.BasePermission):
    """
    Determine if user has access to officer menu
    """

    def has_permission(self, request, view):
        
        user_permissions = []
        for p in request.user.get_all_permissions():
            user_permissions.append(p)

        view_permission = "main.can_access_officer_menu"
        return view_permission in user_permissions