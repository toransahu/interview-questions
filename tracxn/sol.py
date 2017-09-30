#!bin/python3

#if msg is the encrypted message string, then

msg_list = msg.split('.')
decrypted_msg = ''

pad_count = 0
pad_flag = True

for word in msg_list:
    for i in range(len(word),0):
        if(int(word[i-1] + 2) == int(word[i])):
            idx = i-1
            pad_count+=1
        else:
            pad_flag = False
            break
    if(pad_count>=2 and pad_flag == True):
        decrypted_msg = decrypted_msg + word[0:idx] + '.'
    else:
        decrypted_msg = decrypted_msg + word + '.'

decrypted_msg = decrypted_msg.strip('.')

valid_flag = True
for word in decrypted_msg:
    if(validate(word)):
        pass
    else:
        valid_flag = False
        break

print("The original msg was: ",msg," , and processed msg is :",decrypted_msg," whose validity is:",valid_flag)


def validate(word):
