################################################################################
# Author: BO-YANG WU
# Date: 02/20/2020
# This program predicts the approximate size of a population of organisms.
################################################################################

def get_valid_score():#re print the question
    n= int(input('Enter a score: ')) 
    while n< 0 or n> 100:
        print('Invalid Input. Please try again.', end='')
        n= int(input('Enter a score: '))
    return n
    
def calc_average(l):#cal avg
    return sum(l)/ len(l)
    
    
def determine_grade(g):# A B C D
    if g>= 90:
        return 'A'
    elif g>= 80:
        return 'B'
    elif g>= 70:
        return 'C'
    elif g>= 60:
        return 'D'
    else:
        return 'F'

number=[0]* 5
for i in range(0,5):
    number[i]=get_valid_score()
    print('The letter grade for', format(number[i], '.1f'), 'is', determine_grade(number[i]), end='')
    print('.', end='')
print('')
print('The average test score is', format(calc_average(number), '.2f')) # print out the average result
    
      


    
    
    