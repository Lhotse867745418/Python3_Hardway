#-------------------------------------------------------------------------------
# Name:        ask questions
# Purpose:     get input from person
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

## end = ' ' at the end of each print line
## this tells print to not end the line with a newline character
## and go to the next line.

print("how old are you?", end = ' ')

age = input()

print("how tall are you?", end = ' ')

##height = input()
## convert string to int data type
height = int( input() )

print("how much do you weigh?", end = ' ')

##weight = input()
weight = int( input() )

weight_factor = (height - 105) / (1.05 * weight)

print(f"so, you'are {age} old, {height} cm and {weight} kg.your weight factor is {weight_factor}")


def main():
    pass

if __name__ == '__main__':
    main()