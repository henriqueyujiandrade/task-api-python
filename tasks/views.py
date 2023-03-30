from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from .permissions import IsTaskOwner

from .models import Task
import ipdb
from .serializers import TaskSerializer, TaskPatchSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

    def get_queryset(self):

        return self.queryset.filter(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTaskOwner]
    serializer_class = TaskPatchSerializer
    queryset = Task.objects.all()

    lookup_url_kwarg = "pk"


