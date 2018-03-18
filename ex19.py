#-------------------------------------------------------------------------------
# Name:        functions and variables
# Purpose:     define function
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party")
    print("get a blanket.\n")


print("we can just give the function nubers directly:")

cheese_and_crackers(20,30)


print("or, we can use variables from our script:")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can math inside too:")

cheese_and_crackers(20 + 10, 20 + 3)


print("and we combine the two, variable and math:")


cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 100)



def main():
    pass

if __name__ == '__main__':
    main()
