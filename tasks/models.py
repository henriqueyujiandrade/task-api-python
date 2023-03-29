from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tasks", null=True
    )
