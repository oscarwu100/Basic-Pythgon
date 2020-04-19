################################################################################
# Author: BO-YANG WU
# Date: 02/05/2020
# This program calculate the days of February of each year
################################################################################


year= int(input('Please input a year:'))
if year% 400== 0:
    days= 29
elif year% 100== 0:
    days= 28
elif year% 4== 0:
    days= 29
else:
    days= 28

print('In the year', year, end='')
print(', February has', days,'days.')