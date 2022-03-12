from pyexpat import model
from django.db import models

# Create your models here.

class customer(models.Model):
    cust_name = models.CharField(max_length=30)
    cust_city = models.CharField(max_length=40)