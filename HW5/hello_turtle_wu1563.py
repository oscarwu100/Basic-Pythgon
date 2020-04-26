################################################################################
# Author: BO-YANG WU
# Date: 02/25/2020
# This program is to write “hello turtle” on the screen
################################################################################

def h():
    right(90)
    forward(50)
    right(180)
    forward(15)
    left(180)
    circle(15, -180)
    left(180)
    forward(15)

def e():
    circle(15, -270)
    left(90)
    forward(30)
    
def l():
    left(90)
    forward(50)
    
def o():
    circle(15, 360)
    
def t():
    left(90)
    forward(50)
    left(180)
    forward(20)
    left(90)
    forward(10)
    right(180)
    forward(20)
    
def r():
    right(90)
    forward(30)
    right(180)
    forward(15)
    left(180)
    circle(10, -90)
    left(180)
    forward(15)
    
def u():
    right(90)
    forward(30)
    left(180)
    forward(10)
    circle(15, -180)
    left(180)
    forward(20)

from turtle import *
setup(900,900)
color('black')
shapesize(2,2)
width('7')
hideturtle()

penup() 
goto(-200, 200)
pendown() 
h()

penup() 
left(90)
goto(-130, 150)
pendown() 
e()

penup() 
goto(-90, 200)
pendown() 
l()

penup() 
right(90)
goto(-60, 200)
pendown() 
l()

penup() 
goto(-30, 165)
pendown() 
o()

penup() 
left(90)
goto(-190, 70)
pendown() 
t()

penup() 
left(180)
goto(-130, 100)
pendown() 
u()

penup() 
right(90)
goto(-100, 100)
pendown() 
r()

penup() 
goto(-50, 70)
pendown() 
t()

penup() 
goto(-20, 120)
pendown() 
l()

penup()
left(90) 
goto(10, 70)
pendown() 
e()

done()