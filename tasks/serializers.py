from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "description",
            "status",
            "created_at",
            "updated_at",
            "user"
        ]
        read_only_fields = ["created_at","status","updated_at"]
        extra_kwargs = {"user": {"write_only": True}}

class TaskPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "description",
            "status",
            "created_at",
            "updated_at",
            "user"
        ]
        read_only_fields = ["created_at","updated_at", "user"]

