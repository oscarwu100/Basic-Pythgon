################################################################################
# Author: BO-YANG WU
# Date: 02/11/2020
# This program calculate some number
################################################################################


num= float(input('Enter a positive number (negative to quit):'))

n= 1
i= num
while num>= 0:
    num= float(input('Enter a positive number (negative to quit):'))
    if num>= 0:
        i+= num#sum the value
        n+= 1#count how many time it input


print('Sum:', format(i, '.2f'))
print('Average', format(i/ n, '.2f'))