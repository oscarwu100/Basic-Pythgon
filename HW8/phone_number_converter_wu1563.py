################################################################################
# Author: BO-YANG WU
# Date: 03/29/2020
# This program should display the telephone number with any alphabetic characters that
# appeared in the original translated to their numeric equivalent.
################################################################################

import math

telebook= '22233344455566677778889999'
tl= list(telebook)

Tele= input('Enter a telephone number: ')
l= list(Tele) 
new= ""

for i in range(len(l)):
    if ord(l[i])> 96:
        l[i]= ord(l[i])- 97
        l[i]= tl[l[i]]
    elif ord(l[i])> 64:
        l[i]= ord(l[i])- 65
        l[i]= tl[l[i]]
    new+= str(l[i])
    
print("The phone number is", new)
