'''
Created on 30-Nov-2016

@author: toran
'''

d=open('input.txt').read()
d2=(d.split('\n'))
print(d2[1])
for i in d2[1].split(','):
    print(i)