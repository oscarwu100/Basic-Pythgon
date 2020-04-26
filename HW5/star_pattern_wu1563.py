################################################################################
# Author: BO-YANG WU
# Date: 02/24/2020
# This program is to  draw the star by having the turtle trace its perimeter
################################################################################

from turtle import *
setup(900,900)
color('black')
shapesize(2,2)
width('7')

p= int(input('Input the points: '))
a= 360/ p
b= 2* a

begin_fill()
left(b/ 2)
forward(50)
for i in range(p):
    left(180- a)
    forward(50)
    right(180- b)
    forward(50)

color('pink')
end_fill()

done()