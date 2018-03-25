#-------------------------------------------------------------------------------
# Name:        is-a and has-a
# Purpose:     understand class and objects
#
# Author:      Administrator
#
# Created:     25/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------



## animal is-a object (yes,sort of confusing) look at the extra credit

class Animal(object):
    pass

## ??

class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has-a pet of some kind
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what id this  strange magic?
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is a dog

rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()
                           .
## ??
crouse = Salmon()

## ??
harry = Halibut()








def main():
    pass

if __name__ == '__main__':
    main()
