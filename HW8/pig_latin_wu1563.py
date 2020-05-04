################################################################################
# Author: BO-YANG WU
# Date: 03/29/2020
# This program is to  accepts a sentence as input and converts each word to
# “Pig Latin.”
################################################################################
import re

s= input('Enter a string: ')

p = re.compile("((\w)+)") 
s1 = p.sub(lambda a : a.group()[1:]+ a.group()[0]+ 'ay', s) 

print(s1.capitalize())