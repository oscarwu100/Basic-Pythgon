################################################################################
# Author: BO-YANG WU
# Date: 03/29/2020
# This program is to reads the random numbersfrom the random_numbers.txt
# file you created in Exercise 4.
################################################################################

f= open("random_numbers.txt")
f1= f.read()

num= f1.split()

for i in range(len(num)):
    num[i]= int(num[i])

print(format(len(num), ',d'), 'numbers were read from the file.')
print('Max: ', max(num))
print('Min: ', min(num))
print('Sum: ', format(sum(num), ',d'))
print('Avg: ', format(sum(num)/ len(num), ',.1f'))
