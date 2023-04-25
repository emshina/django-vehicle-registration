from django.db import models
# from .import models

# Create your models here.
class car_owner(models.Model):
    Number_plate = models.CharField(max_length=8 ,primary_key=True)
    Phone_number = models.IntegerField()
    ID = models.IntegerField()
    
class Meta:
    manage=False
    db_table='car_owner'