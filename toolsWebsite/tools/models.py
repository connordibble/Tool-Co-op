from django.db import models
from django.db.models import ImageField


class ToolCategory(models.Model):
    type = models.CharField(max_length=30)
    available = models.IntegerField(default=0)
    unavailable = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    tool_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='')


