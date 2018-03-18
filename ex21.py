#-------------------------------------------------------------------------------
# Name:        functions can return something
# Purpose:     use function to return some value and  caculate something
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------


def add(a, b):
    print(f"adding： {a} + {b} = {a + b}")
    return a + b


def substract(a, b):
    print(f"substracting： {a} - {b} = {a - b}")
    return a - b


def multiply(a, b):
    print(f"multiplying: {a} * {b} = {a * b} ")
    return a * b


def divide(a, b):
    print(f"dividing: {a} / {b} = {a / b} ")
    return a / b


print("let's do some math with just functions!")


age = add(30, 5)

height = substract(78, 4)

weight = multiply(90, 2)

iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, IQ: {iq}")


print("here is a puzzle.")

print("can you caculate this? add(age, substract(height, multiply(weight, divide(iq, 32))))")

what = add(age, substract(height, multiply(weight, divide(iq, 32))))

print(f"let me tell you the result. that is becomes: {what} , can you do it by hand?")


def main():
    pass

if __name__ == '__main__':
    main()