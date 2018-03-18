#-------------------------------------------------------------------------------
# Name:        names, variables, code, functions
# Purpose:     define function
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------


# this one is like your scripts with argv

def print_two( *args ):
    arg1, arg2 = args
    print(f"arg1: {arg1},arg2:{arg2}")

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1},arg2:{arg2}")

# this just takes one argument

def print_one( arg1 ):
    print(f"arg1: {arg1}")

# this one takes no aruments

def print_none():
    print("i got nothing.")



print_two("zed","aea")

print_two_again("leo", "ted")

print_one("love you")

print_none()




def main():
    pass

if __name__ == '__main__':
    main()