'''
Created on 10-Nov-2016

@author: toran
'''

lst=[1,3,9,4,6,7,5,8,2]

s=10

for i in lst:
    if lst.count(s-i)>=1:
        print(i, s-i)
        
        