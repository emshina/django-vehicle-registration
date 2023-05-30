
from django.utils import timezone
from django.db import models
# from .import models

# Create your models here.
# class car_owner(models.Model):
#     Number_plate = models.CharField(max_length=8 ,primary_key=True)
#     Phone_number = models.IntegerField()
#     ID = models.IntegerField()
    
# class Meta:
#     manage=False
#     db_table='car_owner'


class Identification(models.Model):
    ID = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=80)

class Phone_Number(models.Model):
    ID= models.ForeignKey(Identification,on_delete=models.PROTECT)
    Phone_Numbers=models.IntegerField(max_length=13)


class Registration(models.Model):
    Number_Plate =models.CharField(max_length=10, primary_key=True)
    ID = models.ForeignKey(Identification,on_delete=models.PROTECT)
    email=models.EmailField(max_length=254)
    # date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=timezone.now)
    

    
 
class County(models.Model):
    county_code = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=20)
    
class Police_station(models.Model):
    Police_station_code = models.IntegerField(primary_key=True)
    station_name = models.CharField( max_length=50)
    county = models.ForeignKey(County,on_delete=models.PROTECT)
    sub_county= models.CharField(max_length=30, null=True)
    ward =models.CharField(max_length=30, null=True)
    Phone_Number = models.IntegerField(max_length=13, null=True)
    
    
class Charges(models.Model):
    Number_Plate = models.ForeignKey(Registration,on_delete=models.PROTECT)      
    Police_station_code = models.ForeignKey(Police_station,on_delete=models.PROTECT)
    Charges= models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    
    
# class Messages(models.Model):
    
    
    
    