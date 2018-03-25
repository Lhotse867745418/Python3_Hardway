#-------------------------------------------------------------------------------
# Name:        what if
# Purpose       if-elif-elsestatement
#
# Author:      lhotse
#
# Created:     19/03/2018
# Copyright:   (c) Administrator 2018
# Licence:
#-------------------------------------------------------------------------------

people = 30

cats = 30

dogs = 15


if people < cats:
    print("too many cats! the world is doomed")
elif people > cats:
    print("not many cats! the world is saved!")
else:
    print("every one will have one cat!" )


if people < dogs:
    print("the world is drooled on!")
elif people > dogs:
    print("the world is dry!")
else:
    print("the amount of people is same as dogs！")

def main():
    pass

if __name__ == '__main__':
    main()
