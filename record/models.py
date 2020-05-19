from django.db import models
from rest_framework import permissions
from datetime import datetime
import os
import uuid

# permission_classes = [permissions.IsAuthenticated]
def get_upload_path():
    return os.path.join('record/', datetime.now().date().strftime("%Y/%m/%d"))


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    time = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to=get_upload_path())
    class Meta:
        ordering = ['time']
