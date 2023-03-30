from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Task


class IsTaskOwner(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        task: Task,
    ) -> bool:
        
        return task.user == request.user