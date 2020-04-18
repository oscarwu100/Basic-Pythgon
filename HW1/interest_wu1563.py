################################################################################
# Author: BO-YANG WU
# Date: 01/30/2020
# This program calculate it pays interest not only on the
# principal amount that is deposited into the account
################################################################################


print('Enter the following quantities in feet.')
P= float(input('How much is the initial deposit?'))#amount of principal originally deposited
r= float(input('What is the annual interest rate in percent?'))# annual interest rate paid by the account
n= int(input('How many times per year is the interest compounded?'))#  number of times per year that the interest is compound
t= float(input('How may year will the account be left to earn interest?'))# number of years the account will be left to earn interest

r= r/ 100 #percentage

FV=P* pow((1+ r/ n), (n* t))

print('At the end of', float(t), 'years the account will be worth $',end= '')
print(format(FV, ',.2f'))