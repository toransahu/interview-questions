'''
Created on 10-Nov-2016

@author: toran
'''

s1="promptcloudp"
s2="clduoportmpc"

t=0
if(len(s1)==len(s2)):
    for i in s1:
        if(s2.count(i)==s1.count(i)):
            t=1
    if(t==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")

                