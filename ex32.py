#-------------------------------------------------------------------------------
# Name:        loops and lists
# Purpose:     for statement, and lists
#
# Author:      lhotse
#
# Created:     20/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

the_count = [1, 2, 3, 4, 5]

fruits = ['apples', 'oranges','pears','apricots']

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"this is count {number}")

# same as above

for fruit in fruits:
    print(f"a fruit of type: {fruit}")


# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it

for i in change:
    print(f"i got {i}")


# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to counts

for i in range(0, 6):
    print(f"adding {i} to the list.")

    # append is a function that lists understand

    elements.append(i)

# now we can print then out too

for  i in elements:
    print(f"elements was: {i} ")

def main():
    pass

if __name__ == '__main__':
    main()
