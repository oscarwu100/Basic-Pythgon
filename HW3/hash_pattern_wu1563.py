################################################################################
# Author: BO-YANG WU
# Date: 02/11/2020
# This program print number of line tree
################################################################################


num= int(input('Enter the number of lines:'))

for i in range(num):
    print('*', end='')#print first *
    for j in range(i):
        print(' ', end='')#print space
    print('*')#print last *
