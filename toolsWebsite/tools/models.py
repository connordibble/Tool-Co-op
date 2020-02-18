from django.db import models

class ToolCategory(models.Model):
    type = models.CharField(max_length=30)
    available = models.IntegerField(default=0)
    unavailable = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


