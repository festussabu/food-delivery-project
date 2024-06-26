from django.db import models
from user_app.models import Customer

# Create your models here.
class Vendor(models.Model):
  vendor_name = models.CharField(max_length=25)
  vendor_email = models.EmailField()
  vendor_password = models.CharField(max_length=25)
  vendor_approval_status = models.BooleanField(default=False)

  def __str__(self):
    return self.vendor_name

class FoodItem(models.Model):
  vendor_name = models.CharField(max_length=40, default='')
  food_image = models.ImageField()
  food_name = models.CharField(max_length=25)
  food_category = models.CharField(max_length=20)
  food_price = models.IntegerField()
  resturant_name = models.CharField(max_length=200, default='')
  station_name = models.CharField(max_length=200, default='')

  def __str__(self):
    return self.food_name
