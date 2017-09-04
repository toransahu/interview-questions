'''
Created on 23-Oct-2016

@author: toran
'''

input=open("input.txt").read().splitlines()

bags=input[0]
balls=sorted(list(map(int, input[1].split(','))))
players=input[2]

dict={}
for i in range(0,len(balls) -1):
    if i>=(int(bags)-int(players)+1):
        break
    diff=balls[i+int(players)-1]-balls[i]
    dict[str(i)]=diff
#print(sorted(dict.values())[0])

output=open("output.txt","w")
result=""
for key, value in dict.iteritems():
    if(value==sorted(dict.values())[0]):
        for i in range(0,int(players)):
            if(i==int(players)-1):
                result+=str(balls[int(key)+i])
            else:
                result+=str(balls[int(key)+i]) + "," 
output.write(result)
        
        
        