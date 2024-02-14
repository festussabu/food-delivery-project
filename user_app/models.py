from django.db import models

# Create your models here.
class Customer(models.Model):
  username = models.CharField(max_length=25)
  email = models.EmailField()
  password = models.CharField(max_length=25)
  pnr_number = models.CharField(max_length=4)
  train_number = models.IntegerField()

