#-------------------------------------------------------------------------------
# Name:        while loops
# Purpose:
#
# Author:      lhotse
#
# Created:     21/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

i = 0

numbers = []

while i <  6:
    print(f"at the top i is {i}.")

    numbers.append(i)

    i += 1

    print("numbers now:", numbers)

    print(f"at the bottom i is {i}")

    print("the numbers:")



for num in numbers:
    print(num)



def main():
    pass

if __name__ == '__main__':
    main()
