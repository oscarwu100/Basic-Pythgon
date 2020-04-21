################################################################################
# Author: BO-YANG WU
# Date: 02/12/2020
# This program calculate some number
################################################################################

month= ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.',
        'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
rain= [0]* 12
j= 0

for i in month:
    rain[j]= float(input('Enter the rainfall amount for', format(str(i)),':'))
    j+= 1
    
    
