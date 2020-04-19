################################################################################
# Author: BO-YANG WU
# Date: 02/05/2020
# This program calculate the discount of the sale price
################################################################################


packages= int(input('Please input the number of packages to be purchased:'))

if packages<= 0:
    print('Invalid Input!')
elif packages< 10:
    print('No discount applied.')
    print('The final price for purchasing', packages,'packages is $', end= '')
    print(format(99* packages,'.2f'))
elif packages< 20:
    print('10% discount applied.')
    print('The final price for purchasing', packages,'packages is $', end= '')
    print(format(99* packages* 0.9,'.2f'))
elif packages< 50:
    print('25% discount applied.')
    print('The final price for purchasing', packages,'packages is $', end= '')
    print(format(99* packages* 0.75,'.2f'))
elif packages< 100:
    print('35% discount applied.')
    print('The final price for purchasing', packages,'packages is $', end= '')
    print(format(99* packages* 0.65,'.2f'))
else:
    print('45% discount applied.')
    print('The final price for purchasing', packages,'packages is $', end= '')
    print(format(99* packages* 0.55,'.2f'))