#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:15:49 2017

@author: toran
"""

from django.db import models

# =============================================================================
# class Weather(models.Model):
#     region = models.CharField(max_length=15)
#     attribute = models.CharField(max_length=15)
#     season = models.CharField(max_length=4)
#     year = models.IntegerField(default=0)
#     value = models.FloatField(default=0)
#     
#     
# =============================================================================
    
class Climate(models.Model):
    region = models.CharField(max_length=15)
    season = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    tmin = models.FloatField(default=0)    
    tmean = models.FloatField(default=0)    
    tmax = models.FloatField(default=0)    
    sunshine = models.FloatField(default=0)    
    rainfall = models.FloatField(default=0)    
    
    def __str__(self):
        return self.region, self.season, self.year, self.tmin, self.tmean, self.tmax