################################################################################
# Author: BO-YANG WU
# Date: 03/29/2020
# This program is to asks the user how many numbers it should generate and
# then writes that many random numbers to a file named random_numbers.txt.
################################################################################

import random as r


f= open("random_numbers.txt", "w+")

n= int(input('Enter the number of random numbers to be written to the file: '))

for i in range(n- 1):
    num= r.randrange(1, 501)
    f.write(str(num))
    f.write("\n")
    
num= r.randrange(0, 501)
f.write(str(num))
f.close()