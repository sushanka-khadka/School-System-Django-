from django.db import models
from django.conf import settings
import uuid
# Create your models here.

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ ' '.join([self.user.first_name, self.user.last_name]) if (self.user.first_name or self.user.last_name) else 'Unknown'}: {self.message}"