#-------------------------------------------------------------------------------
# Name:        reading files
# Purpose:     reading file and print content
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

txt = open(file_name)



prompt ='>'

print (f"here is your file  {file_name}:")


print(txt.read())


print("type the filename again:")


file_again = input(prompt)


txt_again = open(file_again)

print(txt_again.read())


txt.close()

txt_again.close()

def main():
    pass

if __name__ == '__main__':
    main()