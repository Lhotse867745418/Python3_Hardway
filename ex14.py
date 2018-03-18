#-------------------------------------------------------------------------------
# Name:        prompting and passing
# Purpose:     get argv from commad line of power shell
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

##import sys

##script = sys.argv


# read the wyss section for how to run this


from sys import argv

script, user_name = argv

prompt ='>'

print (f"hi {user_name}, i'm the {script} script.")

print("i'd like to ask you a few questions.")

print(f"do you like me {user_name}")

likes = input(prompt)

print(f"where do you live {user_name}")

lives = input(prompt)

print("what kind of computer do you have?")

computer = input(prompt)

print(f"""
alright, so you said {likes} about like me.
you live in {lives}. not sure where that is.
and you have a {computer} computer.
Nice """)


def main():
    pass

if __name__ == '__main__':
    main()