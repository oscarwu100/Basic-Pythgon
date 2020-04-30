################################################################################
# Author: BO-YANG WU
# Date: 03/19/2020
# This program is to write a function that accepts two arguments: 
# a list, and a number
################################################################################


def listnumber(l, n):
    a= []
    print("Number: ", n)
    print("List of numbers:")
    print(l)
    for i in range(0, len(l)):
        if l[i]> n:
            a.append(l[i])
    print("Numbers in list that are larger than", n, end='')
    print(":")
    print(a)
    
l= [19, 2940, 10, 24, 29, 1, 85, 201, -15, -122, 799]
n= 13
listnumber(l, n)