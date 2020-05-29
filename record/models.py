from django.db import models
from django.utils import timezone
import os, uuid


def get_upload_path():
    return os.path.join('record/', timezone.now().date().strftime("%Y/%m/%d"))


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to=get_upload_path())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time']
