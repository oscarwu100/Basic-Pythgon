################################################################################
# Author: BO-YANG WU
# Date: 03/19/2020
# write function called roll_d6 that simulates a single six-sided
# die roll by returning a random integer between 1 and 6 (inclusive). 
################################################################################

import random as r

def roll_d6():
    num= r.randrange(1, 7)
    return num

l= [0]* 13

for i in range(1000000):
    n1= roll_d6()
    n2= roll_d6()
    l[n1+ n2]= l[n1+ n2]+ 1

print("Roll: Frequency")

for i in range(2, 13):
    print("   "+ str(i) +":", format(l[i]/10000, '.2f')+ "%")
 


