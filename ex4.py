#-------------------------------------------------------------------------------
# Name:        variables and names
# Purpose:     learn variables and names
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------

cars = 100

space_in_a_car = 4.0

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven


print("thern are ", cars, " cars available.")

print("thern are ", drivers, " drives available.")

print("thern are ", cars_not_driven, " empty cars today.")

print("we can drive ", carpool_capacity, " people today.")

print("we have ", passengers, " to carpool today.")

print("we need to put about ", average_passengers_per_car, " in each car.")



def main():
    pass

if __name__ == '__main__':
    main()