'''
Created on 23-Oct-2016

@author: toran
'''

from exceptions import ValueError


input_data= open("input.txt").read().splitlines()
output_data=open("output.txt","wb+")


lst=input_data[0]

for i   in range(1,len(input_data)):
    try:
        if(type(int(input_data[i])) is int):
            if(input_data[0].count(input_data[i])>1):
                print("Exception : "+ input_data[i] + " is a duplicate entry!")
                output_data.write("Exception : "+ input_data[i] + " is a duplicate entry!\n") 
            elif(input_data[0].count(input_data[i])==0):
                print("Exception : "+input_data[i]+" is not in the list!")
                output_data.write("Exception : "+input_data[i]+" is not in the list!\n")
            else:
                supporter= int( input_data[i]) + len( ('{0:08b}'.format(int(input_data[i]))).lstrip("0"))
                if(input_data[0].count(str(supporter))>=1):
                    print(input_data[i] + " is SUPPORTED BY THE NUMBER " + str(supporter))
                    output_data.write(input_data[i] + " is SUPPORTED BY THE NUMBER " + str(supporter) +"\n")
                else:
                    print(input_data[i] + " is NOT SUPPORTED")
                    output_data.write(input_data[i] + " is NOT SUPPORTED\n")
    except ValueError :
        if((type(input_data[i]) is str) and input_data[i].strip()==''):
            print("No input provided!")
            output_data.write("No input provided!\n")
        else:
            print("Exception : "+ input_data[i] +" is a string!")
            output_data.write("Exception : "+ input_data[i] +" is a string!\n")

output_data.close()


