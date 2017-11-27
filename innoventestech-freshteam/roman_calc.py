# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:44:06 2017

@author: toran.sahu
"""

r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

d_r = {1: 'I', 5: 'V', 10: 'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

r1 = "CMXXXIX"
r2 = "MMMCMXL"
r3 = "IIII"


def roman_to_decimal(roman_num):
    """Convert a roman number to a decimal number."""
    ## N is number in decimal
    ## initialize N with last element of the roman number
    N = r_d[roman_num[-1]] 
    
    ## loop through each elements in reverse order
    ## from second last element to first element
    for i in range(len(roman_num) - 2, -1, -1):
        ## if current digit is less than RHS element 
        ## substract it from N
        ## else add it to N
        if r_d[roman_num[i]] < r_d[roman_num[i + 1]]:
            N = N - r_d[roman_num[i]]
        else:
            N = N + r_d[roman_num[i]]
    return N


def decimal_to_roman(dec_num):
    """Convert a decimal number to a roman number."""
    rem = 0 ## reminder
    quo = 0 ## quotient
    R = '' ## roman number as a string
    
    
    
    
    
    
    
    
    
    
    for i in [1000,500,100,50,10,5,1]:
        quo = dec_num//i
        if quo>=1:
            dec_num -= i * quo
            break
    