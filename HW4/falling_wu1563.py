################################################################################
# Author: BO-YANG WU
# Date: 02/15/2020
# This program calculate rainfall
################################################################################

def falling_distance(t):#count
    return 1/ 2* 9.81* t* t
    

print('Time (s)   Distance (m)')
print('-----------------------')

for i in range(1, 10):#for loop
    print('      ', i, '       ', format(falling_distance(i), '6.2f'))
