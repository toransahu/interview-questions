# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:18:53 2017

@author: toran.sahu
"""

from download_data import regions, attributes
import pandas as pd

loc = "D:\Toran\WorkSpace\practice\interview\kisanhub\data"
file_loc = loc + '\Tmax_UK.txt'

cols = [
    'JAN', 'Year', 'FEB', 'Year', 'MAR', 'Year', 'APR', 'Year', 'MAY', 'Year',
    'JUN', 'Year', 'JUL', 'Year', 'AUG', 'Year', 'SEP', 'Year', 'OCT', 'Year',
    'NOV', 'Year', 'DEC', 'Year', 'WIN', 'Year', 'SPR', 'Year', 'SUM', 'Year',
    'AUT', 'Year', 'ANN', 'Year'
]
dataframe = pd.read_csv(file_loc, sep='\s+', names=cols)
dataframe = dataframe[pd.notnull(dataframe)]
print(dataframe)
