# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:44:06 2017

@author: toran.sahu
"""

def roman_to_decimal(roman_num):
    """Convert a roman number to a decimal number."""
    
    r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
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
    
    R ='' # created empty string to store roman number
    
    # iterate through each place holder like in 3941: 3000, 900, 40, 1
    # convert them indually to roman & add/concatenate together
    for i,ch in enumerate(str(dec_num)):
        dec = 10**(len(str(dec_num))-i-1) * int(ch)
        r = ''
        if dec >= 1000:
            r =  d_r[1000] * (dec//1000)
        elif dec <1000 and dec >=500:
            if dec<900:
                sub = dec-500
                r =  'D' + 'C' * (sub//100)
            else:
                r =  'CM'
        elif dec <500 and dec >=100:
            if dec<400:
                sub = dec-100
                r =  'C' + 'C' * (sub//100)
            else:
                r =   'CD'
        elif dec <100 and dec >=50:
            if dec<90:
                sub = dec-50
                r =  'L' + 'X' * (sub//10)
            else:
                r =   'XC'
        elif dec <50 and dec >=10:
            if dec<40:
                sub = dec-10
                r =  'X' + 'X' * (sub//10)
            else:
                r =   'XL'
        elif dec <10 and dec >=5:
             if dec<9:
                sub = dec-5
                r =  'V' + 'I' * (sub)
             else:
                r =   'IX'
        elif dec <5 and dec >=1:
            if dec<4:
                sub = dec-1
                r =  'I' + 'I' * (sub)
            else:
                r =   'IV'
        R += r
    return R

if __name__ == '__main__':
    print(decimal_to_roman(3941))
    print(roman_to_decimal('MMMCMXLI'))