from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    ref = models.CharField(max_length=9)
    cost = models.FloatField()
    price = models.FloatField()
    
    def __str__(self):
        return str(self.id)

