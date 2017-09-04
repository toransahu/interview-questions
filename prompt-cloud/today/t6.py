'''
Created on 30-Nov-2016

@author: toran
'''
from multiprocessing import Pool

def f(x):
    return x*x

print(map(f, [1, 2, 3]))