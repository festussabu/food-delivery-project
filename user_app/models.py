from django.db import models

# Create your models here.
class Customer(models.Model):
  username = models.CharField(max_length=25)
  email = models.EmailField()
  password = models.CharField(max_length=25)
  train_number = models.IntegerField()

  def __str__(self):
    return self.username


class Order(models.Model):
  train_number = models.CharField(max_length=10)
  customer_name = models.CharField(max_length=25)
  product_name =  models.CharField(max_length=25)
  price =  models.CharField(max_length=25)
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.customer_name
  
  