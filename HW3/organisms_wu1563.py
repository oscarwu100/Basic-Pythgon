################################################################################
# Author: BO-YANG WU
# Date: 02/13/2020
# This program predicts the approximate size of a population of organisms.
################################################################################

pop= int(input('Starting number of organisms: '))#input start
percent= int(input('Average daily increase, in percent: '))#input percent
day= int(input('Number of days to multiply: '))#input days

print('Day   Approx. Pop')

for i in range(1, day+ 1):
    if i== 1:
        pop= pop
    else:
        pop= pop* (1+ percent/ 100)#claculate
    print(format(i, '2'), format(pop, '14.4f'))#output