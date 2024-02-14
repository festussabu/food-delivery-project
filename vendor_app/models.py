from django.db import models
from user_app.models import Customer

# Create your models here.
class Vendor(models.Model):
  vendor_name = models.CharField(max_length=25)
  vendor_email = models.EmailField()
  vendor_approval_status = models.BooleanField(default=False)

class FoodItem(models.Model):
  food_name = models.CharField(max_length=25)
  food_description = models.CharField(max_length=50)
  food_price = models.IntegerField()
  food_availability = models.BooleanField(default=True)
  vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  ordered_item = models.CharField(max_length=25)
  delivery_address = models.CharField(max_length=100)