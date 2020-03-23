from django.db import models
from datetime import date
from django.db.models import ImageField
import json

class ToolCategory(models.Model):
    type = models.CharField(max_length=30)
    available = models.IntegerField(default=0)
    unavailable = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    tool_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='')

class DueDates(models.Model):
    toolCategory = models.ForeignKey(ToolCategory,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    buyer = models.CharField(max_length=200)
    date_bought = models.DateTimeField()
    date_due = models.DateTimeField()

class ShoppingCart(models.Model):
    toolCategory = models.ForeignKey(ToolCategory, on_delete=models.CASCADE, default=0)
    tool = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)

class History(models.Model):
    customer = models.CharField(max_length=200)
    date_bought = models.DateTimeField()
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    tools = models.CharField(max_length=500)
    CHECKIN = "Checked In"
    CHECKOUT = "Checked Out"
    
    state = models.CharField(
    max_length=2, default=CHECKOUT)
