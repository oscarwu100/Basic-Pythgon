################################################################################
# Author: BO-YANG WU
# Date: 02/12/2020
# This program calculate rainfall
################################################################################

year= int(input('Enter the number of years: '))#input year
i= 0
total= 0

for i in range(year):
    print('For year NO.', i+ 1)#print NO
    total= total+ float(input('Enter the rainfall amount for Jan.: '))#imput
    total= total+ float(input('Enter the rainfall amount for Feb.: '))
    total= total+ float(input('Enter the rainfall amount for Mar.: '))
    total= total+ float(input('Enter the rainfall amount for Apr.: '))
    total= total+ float(input('Enter the rainfall amount for May.: '))
    total= total+ float(input('Enter the rainfall amount for Jun.: '))
    total= total+ float(input('Enter the rainfall amount for Jul.: '))
    total= total+ float(input('Enter the rainfall amount for Aug.: '))
    total= total+ float(input('Enter the rainfall amount for Sep.: '))
    total= total+ float(input('Enter the rainfall amount for Oct.: '))
    total= total+ float(input('Enter the rainfall amount for Nov.: '))
    total= total+ float(input('Enter the rainfall amount for Dec.: '))

print('There are', year* 12, 'months.')#print
print('The total rainfall is', format(total, '.2f'), 'inches.')
print('The monthly average rainfall is', format(total/ (year* 12), '.2f'), 'inches.')