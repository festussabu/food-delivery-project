from django.db import models

# Create your models here.
class Feedback(models.Model):
  customer_name = models.CharField(max_length=25)
  feedback = models.CharField(max_length=250)
  
  def __str__(self):
    return self.customer_name