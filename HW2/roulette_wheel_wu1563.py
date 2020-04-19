################################################################################
# Author: BO-YANG WU
# Date: 02/05/2020
# This program calculate the pocket number color
################################################################################


num= int(input('Please enter a pocket number:'))

if num< 0:
    print('Invalid Input!')
elif num== 0:
    print('Pocket', num,'is green.')
elif num< 10:
    if num% 2== 0:
        print('Pocket', num,'is black.')
    else:
        print('Pocket', num,'is red.')
elif num< 19:
    if num% 2== 0:
        print('Pocket', num,'is red.')
    else:
        print('Pocket', num,'is black.')
elif num< 29:
    if num% 2== 0:
        print('Pocket', num,'is black.')
    else:
        print('Pocket', num,'is red.')
elif num< 37:
    if num% 2== 0:
        print('Pocket', num,'is red.')
    else:
        print('Pocket', num,'is black.')
else:
    print('Invalid Input!')

