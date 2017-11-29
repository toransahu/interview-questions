#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:15:49 2017

@author: toran
"""

from django.db import models

class Climate(models.Model):
    region = models.CharField(max_length=15)
    attribute = models.CharField(max_length=15)
    