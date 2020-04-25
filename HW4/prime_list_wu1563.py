################################################################################
# Author: BO-YANG WU
# Date: 02/20/2020
# This program predicts the prime number list
################################################################################

def prime_numbers(num):#if is prime
    if num== 1:
        return 0
    for i in range(2, num):
        if num% i == 0:
            return 0
    return 1

n= int(input('Enter a positive integer: '))#input start
print('The primes up to', int(n), 'are: ', end='')
for e in range(2, n+ 1):
    if prime_numbers(e):
        print(int(e), end='')
        if e< n: 
            print(', ',end='')
   