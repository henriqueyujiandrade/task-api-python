from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User

import ipdb

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        
        param_id = view.kwargs["pk"]
        find_user = User.objects.filter(id=param_id)[0]
        
        if request.method == "GET" or request.method == "PATCH":
            if find_user == request.user:
                return True

        return request.user.is_superuser