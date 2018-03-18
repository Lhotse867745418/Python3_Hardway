#-------------------------------------------------------------------------------
# Name:        printing , printing
# Purpose:     learn print grammar
#              formatter function "format" variable into other string
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))

print(formatter.format("one", "two","three","four"))

print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
                      formatter.format("one", "two","three","four"),
                      formatter.format("one", "two","three","four"),
                      formatter.format("one", "two","three","four"),
                      formatter.format("one", "two","three","four")
                      )
     )


print(formatter.format("try your", "own text here", "maybe a poem", "or a song about fear"))


def main():
    pass

if __name__ == '__main__':
    main()