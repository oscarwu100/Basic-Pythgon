################################################################################
# Author: BO-YANG WU
# Date: 03/29/2020
# This program is to reads the contents of a file and tracks the number
# of words and the number of lines in the file.
################################################################################

f= open('rumpelstiltskin.txt')

f1= f.read()

TotalL= f1.count('\n')+ 1

TotalW= f1.split()
n= len(TotalW)

print('Total number of words: ', n)
print('Total number of lines: ', TotalL)
print('Average number of words per line: ', format(n/TotalL, ',.1f'))

