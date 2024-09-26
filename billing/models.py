from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=200)
    
    