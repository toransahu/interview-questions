from django.db import models

# Create your models here.

class Weather(models.Model):
    region = models.CharField(max_length=15)
    attribute = models.CharField(max_length=15)
    season = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    
class Climate(models.Model):
    region = models.CharField(max_length=15)
    season = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    tmin = models.IntegerField(default=0)    
    tmean = models.IntegerField(default=0)    
    tmax = models.IntegerField(default=0)    
    sunshine = models.IntegerField(default=0)    
    rainfall = models.IntegerField(default=0)    