#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:48:12 2017

@author: toran
"""

#from store.models import Climate
import os
from os.path import join, isfile, basename
import csv


def list_files(data_loc):
    """Get downloaded data files."""
    
    files = [join(data_loc, f) for f in os.listdir(data_loc) if isfile(join(data_loc, f))]
    return files


    
def consolidate_data():
    """Save data from CSV to DB"""
    data_loc = "./data"
    #data_loc = "..\..\data"
    files = [file for file in list_files(data_loc) if file.endswith('.csv')]
    final = open('consolidated.csv','w')
    for file in files:
        attribute, region = (os.path.splitext(basename(file))[0]).split('_')
        #print(attribute, region)
        with open(file) as c :
            header = c.readline()
            cols = header.split(',')
            reader = list(csv.reader(c,delimiter=','))
            for i in range(1, len(cols)-1,2):
                season = cols[i]
                for row in reader:
                    val = row[i].strip()
                    year = row[i+1].strip()
                    if val != '':
                        val = float(val)
                    else:
                        val = 9999999
                    if  year != '':
                        #year = int(row[i+1].rstrip('.0'))
                        year = int(float(year))
                    else:
                        year = 9999

                    final.write("'"+region+"',"+"'"+season+"',"+str(year)+",'"+ attribute+"',"+ str(val))
                    final.write('\n')
    final.close()

if __name__ == '__main__':
    data_loc = "..\data"
    consolidate_data()
    #print(list_files(data_loc))
    
