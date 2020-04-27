################################################################################
# Author: BO-YANG WU
# Date: 03/03/2020
# This program is drawing each of the vowels ’a’, ’e’, ’i’, ’o’, ’u’.
################################################################################


import vowels
from turtle import *
setup(900,900)
color('black')
shapesize(2,2)
width('7')
hideturtle()


penup() 
goto(-130, 150)
pendown() 
u()

penup() 
right(90)
goto(-85, 120)
pendown() 
e()

penup() 
right(180)
goto(-50, 120)
pendown() 
i()

penup() 
goto(0, 130)
pendown() 
a()

penup() 
goto(20, 130)
pendown() 
o()


done()
