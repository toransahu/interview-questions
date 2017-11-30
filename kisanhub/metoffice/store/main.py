#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:48:12 2017

@author: toran
"""

from store.models import Climate, Weather

def csv_to_db():
    w = Weather(region='UK', attribute='tmin', season='JAN', year=2017, value=10.10)
    w.save()
    
    return (w.region, w.attribute, w.season, w.year, w.value)

#csv_to_db()
