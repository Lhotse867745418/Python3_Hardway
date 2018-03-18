#-------------------------------------------------------------------------------
# Name:        reading and writing files
# Purpose:     reading file ,writing file
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

script, file_name = argv

print(f"we are going to erase {file_name}.")

print("if you don't want that,hit ctrl-c (^c).")

print("if you do want that, hit return.")

input("?")

print("opening the file...")

target = open(file_name,'w')

print("truncating the file. goodbye!")

target.truncate()

print("now i am goin to ask you for three lines")

line1 = input("line 1:")

line2 = input("line 2:")

line3 = input("line 3:")

line = line1 + "\n" + line2 + "\n" + line3 + "\n"

print("i am going to write these to the file.")

##target.write(line1)
##
##target.write("\n")
##
##target.write(line2)
##
##target.write("\n")
##
##target.write(line3)
##
##target.write("\n")

target.write(line)

print("and finally, we close it.")

target.close()


def main():
    pass

if __name__ == '__main__':
    main()