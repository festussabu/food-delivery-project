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
  food_image = models.ImageField(upload_to='pics')
  food_name = models.CharField(max_length=25)
  food_description = models.CharField(max_length=50)
  food_price = models.IntegerField()
  vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)

  def __str__(self):
    return self.food_name

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  ordered_item = models.CharField(max_length=25)
  delivery_address = models.CharField(max_length=100)

  def __str__(self):
    return self.ordered_item