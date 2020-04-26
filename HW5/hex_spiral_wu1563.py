################################################################################
# Author: BO-YANG WU
# Date: 02/24/2020
# This program is to draw the hexagonal spiral.
################################################################################

from turtle import *
setup(900,900)
color('black')
shapesize(2, 2)
width('7')

forward(5)
for i in range(2, 37):
    left(60)
    forward(5* i)


done()