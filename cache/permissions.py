from rest_framework.permissions import BasePermission

class HasRequiredPermissionForMethod(BasePermission):
    get_permission_required = None
    put_permission_required = None
    post_permission_required = None
    patch_permission_required = None
    delete_permission_required = None

    def has_permission(self, request, view):
        permission_required_name = f"{request.method.lower()}_permission_required"
        if not request.user.is_authenticated and not (
            request.user.is_superuser or request.user.is_staff
        ):
            return False
        if not hasattr(view, permission_required_name):
            view_name = view.__class__.__name__
            self.message = "Access denied. You need permission to access this API."
            return False

        permission_required = getattr(view, permission_required_name)
        if isinstance(permission_required, str):
            perms = [permission_required]
        else:
            perms = permission_required
        if not any(request.user.has_perm(perm) for perm in perms):
            self.message = "Access denied. You need permission to access this API."
            return False
        return True
