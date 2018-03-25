#-------------------------------------------------------------------------------
# Name:        list
# Purpose:
#
# Author:      lhotse
#
# Created:     22/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

ten_things = "apples oranges crows telephone light sugar"

print("wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split(' ')

print("stuff", stuff)

more_stuff = ["day", "night", "song", "frisbee", "corn", "bannana", "girls", "boys"]

print("more_stuff:", more_stuff)

while len(stuff) != 10:

    next_one = more_stuff.pop()

    print("adding:", next_one)

    stuff.append(next_one)

    print(f"there are {len(stuff)} items now.")



print("there we go:", stuff)

print("let's do some things with stuff.")

print(stuff[1])

print(stuff[-1]) # whoa! fancy

print(stuff.pop())

print(' '.join(stuff)) # what ? cool ?

print('#'.join(stuff[3:5])) # super stellar



def main():
    pass

if __name__ == '__main__':
    main()
