################################################################################
# Author: BO-YANG WU
# Date: 01/30/2020
# This program calculate A vineyard owner is 
# planting several new rows of grapevines
################################################################################


print('Enter the following quantities in feet.')
R= int(input('How long is this row?'))#Long
E= int(input('How wide is the end-post assembly?'))#Wide
S= int(input('How much space should be between the vines?'))#space
V= (R- 2* E)/ S

print('This row has enough space for', int(V),'vine(s).')