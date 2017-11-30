# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:18:53 2017

@author: toran.sahu
"""

# from main import regions, attributes


def panda():
    import pandas as pd

    file_loc = "./data"
    file = file_loc + '/Tmax_UK.txt'

    cols = [
        'JAN', 'Year', 'FEB', 'Year', 'MAR', 'Year', 'APR', 'Year', 'MAY',
        'Year', 'JUN', 'Year', 'JUL', 'Year', 'AUG', 'Year', 'SEP', 'Year',
        'OCT', 'Year', 'NOV', 'Year', 'DEC', 'Year', 'WIN', 'Year', 'SPR',
        'Year', 'SUM', 'Year', 'AUT', 'Year', 'ANN', 'Year'
    ]
    dataframe = pd.read_csv(file, sep='\s+', 
                            names=cols, encoding='ANSI')
    print(dataframe)


def csv():
    import csv
    file_loc = "./data"
    file = file_loc + '/Tmax_UK.csv'

    cols = [
        'JAN', 'Year', 'FEB', 'Year', 'MAR', 'Year', 'APR', 'Year', 'MAY',
        'Year', 'JUN', 'Year', 'JUL', 'Year', 'AUG', 'Year', 'SEP', 'Year',
        'OCT', 'Year', 'NOV', 'Year', 'DEC', 'Year', 'WIN', 'Year', 'SPR',
        'Year', 'SUM', 'Year', 'AUT', 'Year', 'ANN', 'Year'
    ]
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        included_cols = [
            0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25,
            27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48, 49
        ]
        included_cols = [
            0
         
        ]
        #reader = csv.DictReader(f)
        for row in reader:
            print(list(row[i].strip() for i in included_cols))
            break


#csv()
panda()
