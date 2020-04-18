################################################################################
# Author: BO-YANG WU
# Date: 01/30/2020
# This program calculate rercipe
################################################################################


Cake=int(input('How many cookies do you want to make?'))

Sugar= Cake/ 48* 1.5
Butter= Cake/ 48* 1
Flour= Cake/ 48* 2.75

print('To make', int(Cake), 'cookies, you will need:')
print(format(Sugar, ',.2f'),'cups of sugar')
print(format(Butter, ',.2f'),'cups of butter')
print(format(Flour, ',.2f'),'cups of flour')