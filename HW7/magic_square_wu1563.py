################################################################################
# Author: BO-YANG WU
# Date: 03/19/2020
# This program is to know Lo Shu Magic Square
################################################################################

l= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Your matrix is:")
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

if (l[0][0] != l[0][1] != l[0][2] != l[1][0] != l[1][1] != l[1][2] != l[2][0] != l[2][1] != l[2][2]) & sum(l[0]) & sum(l[1]) & sum(l[2]) & l[0][0]+ l[1][0]+ l[2][0] & l[0][1]+ l[1][1]+ l[2][1] & l[0][2]+ l[1][2]+ l[2][2] & l[0][0]+ l[1][1]+ l[2][2] & l[0][2]+ l[1][1]+ l[2][0] == 15:
    print("It is a Lo Shu magic square!")
else:
    print("It is not a Lo Shu magic square.")
    
    
print()
l= [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

print("Your matrix is:")
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

if (l[0][0] != l[0][1] != l[0][2] != l[1][0] != l[1][1] != l[1][2] != l[2][0] != l[2][1] != l[2][2]) & sum(l[0]) & sum(l[1]) & sum(l[2]) & l[0][0]+ l[1][0]+ l[2][0] & l[0][1]+ l[1][1]+ l[2][1] & l[0][2]+ l[1][2]+ l[2][2] & l[0][0]+ l[1][1]+ l[2][2] & l[0][2]+ l[1][1]+ l[2][0] == 15:
    print("It is a Lo Shu magic square!")
else:
    print("It is not a Lo Shu magic square.")
    
print()  
l= [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

print("Your matrix is:")
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

if (l[0][0] != l[0][1] != l[0][2] != l[1][0] != l[1][1] != l[1][2] != l[2][0] != l[2][1] != l[2][2]) and (sum(l[0]) & sum(l[1]) & sum(l[2]) & l[0][0]+ l[1][0]+ l[2][0] & l[0][1]+ l[1][1]+ l[2][1] & l[0][2]+ l[1][2]+ l[2][2] & l[0][0]+ l[1][1]+ l[2][2] & l[0][2]+ l[1][1]+ l[2][0])== 15:
    print("It is a Lo Shu magic square!")
else:
    print("It is not a Lo Shu magic square.")