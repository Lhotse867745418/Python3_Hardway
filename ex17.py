#-------------------------------------------------------------------------------
# Name:        more files
# Purpose:     copy one file to another
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

from os.path import exists



script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}.")



# we could do these on on line ,how?

in_file = open(from_file)

in_data = in_file.read()

##in_data = open(from_file).read()




print(f"the input file is {len(indaata)} bytes long.")

print(f"does the output file exist? {exists(to_file)}")

print("ready , hit return to continue, ctrl-c to abort.")

input("go on or cancel?")



out_file = open(to_file, 'w')

out_file.write(in_data)

print ("alright, all done.")



out_file.close()

in_file.close()

def main():
    pass

if __name__ == '__main__':
    main()