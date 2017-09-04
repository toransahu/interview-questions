'''
Created on 10-Nov-2016

@author: toran
'''


inp_lst= open('input.txt').read().splitlines()

#print(inp_lst)

bags=int(inp_lst[0].strip())
balls=[str(i) for i in inp_lst[1].strip().split(',')]
players=int(inp_lst[2])



sorted_balls= (balls)
print(bags,sorted_balls,players)

