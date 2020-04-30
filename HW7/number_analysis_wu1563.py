################################################################################
# Author: BO-YANG WU
# Date: 03/19/2020
# This program asks the users to enter a series of 10 numbers.
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list
################################################################################
l= [0]* 10
for i in range(10):
    l[i]= float(input("Enter number  "+ str(i+ 1) + " of 10: "))
    
print("Lowest number: ", format(min(l), '.2f'))
print("Highest number: ", format(max(l), '.2f'))
print("Total: ", format(sum(l), '.2f'))
print("Average: ", format(sum(l)/ 10, '.2f'))