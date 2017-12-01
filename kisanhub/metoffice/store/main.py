#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:48:12 2017

@author: toran
"""

from store.models import Climate
import os
from os.path import join, isfile, basename
import csv


def list_files(data_loc):
    """Get downloaded data files."""
    
    files = [join(data_loc, f) for f in os.listdir(data_loc) if isfile(join(data_loc, f))]
    return files


def create_or_update(aregion,aseason,ayear,attribute,val):
    """Create or Update record in DB"""
    
    # check for the unique row (region,season,year)
    record = Climate.objects.filter(region = aregion, season = aseason, year = ayear)
    
    if record.exists():
        # update
        if attribute == 'Tmax':
            record.update(tmax = val)
        elif attribute == 'Tmean':
            record.update(tmean = val)
        elif attribute == 'Tmin':
            record.update(tmin = val)
        elif attribute == 'Sunshine':
            record.update(sunshine = val)
        elif attribute == 'Rainfall':
            record.update(rainfall = val)
    else:
        # create
        if attribute == 'Tmax':
            c = Climate(region = aregion, season = aseason, year = ayear, tmax = val)
        elif attribute == 'Tmean':
            c = Climate(region = aregion, season = aseason, year = ayear, tmean = val)
        elif attribute == 'Tmin':
            c = Climate(region = aregion, season = aseason, year = ayear, tmin = val)
        elif attribute == 'Sunshine':
            c = Climate(region = aregion, season = aseason, year = ayear, sunshine = val)
        elif attribute == 'Rainfall':
            c = Climate(region = aregion, season = aseason, year = ayear, rainfall = val)
        c.save()
        return

    
def csv_to_db():
    """Save data from CSV to DB"""
    data_loc = "..\data"
    files = [file for file in list_files(data_loc) if file.endswith('.csv')]
    
    for file in files:
        attribute, region = (os.path.splitext(basename(file))[0]).split('_')
        #region = 'UK'
        #attribute = 'Tmax'        
        with open(file) as c:
            header = c.readline()
            cols = header.split(',')
            for i in range(1, len(cols)-1,2):
                reader = csv.reader(c,delimiter=',')
                season = cols[i]
                for row in reader:
                    val = float(row[i])
                    year = int(row[i+1])
                    create_or_update(region,season,year, attribute, val)
                    

if __name__ == '__main__':
    data_loc = "..\data"
    #csv_to_db(data_loc)
    print(list_files(data_loc))
    
