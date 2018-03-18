#-------------------------------------------------------------------------------
# Name:        more variables and names
# Purpose:     learn variables and names
#              learn format string
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

types_of_people = 10

x  = f"there are {types_of_people} types of people"

binary = "binary"

do_not = "don't"

y = f"those who know {binary} and those who {do_not}."

print(x)

print(y)

print(f"i said:{x}")

print(f"i also said:'{y}'")


##

hilarious = False

joke_evalution = "isn't that joke so funny?! {}"

print(joke_evalution)

print(joke_evalution.format(hilarious))



## string + string

w = "this is the left side of..."

e = "a string with a right side"

print(w + e)




def main():
    pass

if __name__ == '__main__':
    main()