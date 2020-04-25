################################################################################
# Author: BO-YANG WU
# Date: 02/15/2020
# This program predicts the approximate size of a population of organisms.
################################################################################

def max(n1, n2):#find max
    if n2> n1:
        return n2
    else:
        return n1


n1= int(input('Enter the first integer: '))#input start
n2= int(input('Enter the second integer: '))#input percent

print(max(n1, n2), 'is greater.')