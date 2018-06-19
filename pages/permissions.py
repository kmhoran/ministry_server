from rest_framework import permissions


class HasOfficerAccess(permissions.BasePermission):
    """
    Determine if user has access to officer menu
    """
    permission_name = "pages.has_officer_access"
    
    def has_permission(self, request, view):
        
        return self.test_request(request)
    
    def test_request(self, request):
        user_permissions = []
        for p in request.user.get_all_permissions():
            user_permissions.append(p)
        
        return self.permission_name in user_permissions