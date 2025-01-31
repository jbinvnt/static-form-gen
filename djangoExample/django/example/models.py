from django.db import models
from datetime import date
# Create your models here.

class Car(models.Model):
    license_plate = models.CharField(max_length=7)
    vin_number = models.CharField(max_length=17)
    purchase_date = models.DateField(default=date.today) #This demonstrates how after the render, this date will be hardcoded
    miles = models.PositiveIntegerField(default=0)
