################################################################################
# Author: BO-YANG WU
# Date: 03/03/2020
# This program is to move the turtle from the center of the 
# maze to the exit on the right hand side.
################################################################################

import random as r
ans= 4
while ans== 4:
    player= input("Enter rock, paper, or scissors: ")
    if player== 'rock':
        ans= 1
    elif player== 'paper':
        ans= 2
    elif player== 'scissors':
        ans= 3
    else:
        ans= 4
        print("You made an invalid choice. Please try again.")

    num= r.randrange(1, 3)
    if num== 1:
        c= 'rock'
    elif num== 2:
        c= 'paper'
    else:
        c= 'scissors'

    print(" The computer chose", c, end='')
    print(",")
    print(" and you chose", player)

    if num== ans:
        print(" Its a tie. Starting over.")
        ans= 4

if ans== 1 and num== 2:
    print(" The computer won the game.")
elif ans== 1 and num== 3:
    print(" You won the game.")
elif ans== 2 and num== 1:
    print(" You won the game.")
elif ans== 2 and num== 3:
    print(" The computer won the game.")
elif ans== 3 and num== 2:
    print(" You won the game.")
elif ans== 3 and num== 1:
    print(" The computer won the game.")
print("Thanks for playing.")




