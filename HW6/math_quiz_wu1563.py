################################################################################
# Author: BO-YANG WU
# Date: 03/03/2020
# This program is to move the turtle from the center of the 
# maze to the exit on the right hand side.
################################################################################

import random as r
num= r.randrange(0, 999)
num1= r.randrange(0, 999)

print("   ", num)
print("+  ", num1)

ans= int(input())

if ans == num+ num1:
    print("Correct answer -- Good Work!")
else:
    print("Incorrect... The correct answer is: ", num+ num1)