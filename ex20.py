#-------------------------------------------------------------------------------
# Name:        functions and files
# Purpose:     use function read file and prrint file content
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

from sys import argv


script, input_file = argv

def print_all(f):
    print(f.read())

# f.seek(0)  file start from 0 char
# f.seek(x)  file start from x char

def rewind(f):
    f.seek(0)


def print_a_line(line_count,f):
    print(line_count, f.readline())  # what is the meaning of print(arg1, arg2)


current_file = open(input_file)


print("firsr let's print the whole file:\n")


print_all(current_file)


print("now let's rewind, kind of like a tape.")


rewind(current_file)

print("let's print three lines:")

current_line = 1

print_a_line(current_line, current_file)


current_line = current_line + 1

print_a_line(current_line, current_file)


current_line = current_line + 1

print_a_line(current_line, current_file)



def main():
    pass

if __name__ == '__main__':
    main()