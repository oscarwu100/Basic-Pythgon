################################################################################
# Author: BO-YANG WU
# Date: 02/20/2020
# This program predicts the prime number
################################################################################

def is_prime(num):#if is prime
    if num== 1:
        return 0
    for i in range(2, num):
        if num% i == 0:
            return 0
    return 1

n= int(input('Enter a positive integer (-1 quit): '))#input start

while n> 0:# while to print ans
    s= is_prime(n)
    if s:
        print(n, 'is a prime number.', end= '')
    else:
        print(n, 'is not a prime number.', end= '')
    n= int(input('Enter a positive integer (-1 quit): '))#input start