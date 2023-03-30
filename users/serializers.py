from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "updated_at"
        ]
        read_only_fields = ["date_joined", "is_active", "is_staff", "is_superuser","updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_obj = User.objects.create_user(**validated_data)

        return user_obj

class PatchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        ]
        read_only_fields = ["date_joined", "is_active", "is_staff", "is_superuser"]


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        ]
        read_only_fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "date_joined",
            "is_superuser",
        ]
