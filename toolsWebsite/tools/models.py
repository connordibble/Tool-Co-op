from django.db import models
from datetime import date
import json

class ToolCategory(models.Model):
    type = models.CharField(max_length=30)
    available = models.IntegerField(default=0)
    unavailable = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

class DueDates(models.Model):
    toolCategory = models.ForeignKey(ToolCategory,on_delete=models.CASCADE)
    buyer = models.CharField(max_length=200)
    date_bought = models.DateTimeField()
    date_due = models.DateTimeField()


