#-------------------------------------------------------------------------------
# Name:        dictionary, oh lovely dictionary
# Purpose:     learn dictionary data structure
#               "mapping" or "assicilating" is the key concept in a dictionary
# Author:      lhotse
#
# Created:     24/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##stuff = {'name': 'zed', 'age': 39, 'height': 6 * 12 + 2}
##
##print(stuff["age"])
##
##print(stuff['age'])
##
##print(stuff['height'])
##
##
### add a new element to dictionary stuff
##stuff['city'] = "sf"
##
##print(stuff['city'])
##
### add a new element to dictionary stuff
##stuff[1] = "cf"
##
##print(stuff[1])
##
##
### ptint all element of dictionary stuff
##
##print(stuff)
##
### delete a  element from dictionary stuff
##del stuff['city']
##
### ptint all element of dictionary stuff
##
##print(stuff)


# create a mapping of state to abbreviation

states = {'oregon': 'OR', 'florida': 'FL', 'california': 'CA', 'new york': 'NY', 'michigan': 'MI'}

# create a basic set of states and some cities in them

cities = {'CA': 'San Francisco', 'MI':'Detroit', 'FL': 'Jacksonville'}

# add some more cities

cities['NY'] = 'New York'

cities['OR'] = 'Portland'

# print out some cities

print('-' * 10)

print("NY States has:", cities['NY'])

print("OR States has:", cities['OR'])

# print some states

print('-' * 10)

print("michigan's abbreviation is:", states['michigan'])

print("florida's abbreviation is:", states['florida'])

# do it by using the state then cities dict

print('-' * 10)

print("florida has:", cities[states['florida']])

# print every state abbreviation

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


# print every city in state

print('-' * 10)

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

    print('-' * 10)

    # safely get a abbreviation by state that might not be here

state = states.get('Texas')

if not state:
    print("sorry, no Texas")

# get a city with a default value   'Does not exist' is default value

city = cities.get('TX', 'Does not exist')

print(f"the city for the state 'TX' is: {city}")








def main():
    pass

if __name__ == '__main__':
    main()
