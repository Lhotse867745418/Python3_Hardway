#-------------------------------------------------------------------------------
# Name:        gothon games
# Purpose:
#
# Author:      lhotse
#
# Created:     25/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# test ok, no problem


from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):

    def enter(selsf):
        print("this scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "you died. you kinda suck at this.",
        "your mom would be proud... if she were smarter.",
        "such a luser.",
        "i have a small puppy that's better at this.",
        "you're worse than your dad's jokes."
        ]

    def enter(self):

        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)



class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        the gothons of planet percal #25 have invaded estroyed your entire crew. you are the last survive
        member and your last mission is to get the neutron bomb from th weapons armory, put it in the bridge
        blow the ship up after getting into an escape pod
        you are running down the central corridor to the armory when a gothon jumps out, read scaly skin
        teeth, and evil clown costume flowing around h about to pull a weapon to blast you.
        """
        ))

        action = input('shoot! or dodge! or tell a joke! >')

        if action == "shoot!":
            print(dedent("""
            quick on the draw you yank out your blaster
            it at the gothon. his clown costume is flo
            moving aroud his body, which throws off your
            laser hits his constume but misses him this completely ruins his brand
            new costum bought him, which makes him fly into an in and blast you
            repeatly in the face until dead. then he eats you.
            """
            ))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
            like a world class boxer you dodge, weave,slide right as th gothon's
            blaster cranks past your head. in the middle of your artf your foot
            slips and you bang your head on wall and pass out. you wake up shortly
            after die as the gothon stomps on your head
            """
            ))
            return 'death'

        elif action == "tell a joke!":
            print(dedent("""
            lucky for you they made you learn gothon i the academy.
            you tell the one gothon joke lbhe zbgure vf fb sng,jura fur fvgf
            .the gothon stop not to laugh,then busts out laughing and while he's
            laughing you run up and shoot h the head putting him down,then jump througth
            weapon armory door.
            """
            ))
            return 'laser_weapon_armory'

        else:
            print("does not complete!")
            return 'central_corridor'



class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        you do  a dive doll dive roll into the weapon armory,cr
        the room for more gothons that might be hidden quiet
        ,too quiet. you stand up and run to the room and find the neutron
        bomb in its con there's a keypad  lock oon the box and you need get
        the bomb out. if you get the wrong code for 10 times. the lock closes
        forever and you can't get the bomb. the code is 3 digits.
        """
        ))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:

            print("BZZZEDDD!")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:

            print(dedent("""
            the container clicks open and the seal br
            gas out. you grab the neutron bomb and ru
            you can to the bridge where you must place
            right spot.
            """
            ))
            return 'the_bridge'

        else:

            print(dedent("""
            the lock buzzes one last time and then you
            slickening melting sound as te mechanism
            together. you decide to sit there, and fix
            gothons blow up the ship from their ship.
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):

        print(dedent("""
        you burst onto the bridge with the netron destruct bomb
        under you arm and surprises 5 gothons who are take control
        of the ship. each of them has an clown cosstume than the last.
        they haven't pull weapons out yet, as they see the activer bomb
        arm and don't want to set if off.
        """))

        action = input("throw the bomb or slowly place the bomb >")

        if action == "throw the bomb":

            print(dedent("""
            in a panic you throw the bomb at the grou
            and make a leap for the door. right as you
            gothon shoots you right in the back killing
            you die you see another gothon franticall
            disarm the bomb. you die knowing they will blow
            up when it goes off.
            """))
            return 'death'

        elif action == "slowly place the bomb":

            print(dedent("""
            you point your blaster at the bomb under
            the gothons put their hands up  and start
            you inch backward to the door, open it, a
            carefully place the bomb on the floor, po
            blaster at it. you then jump back through
            punch the close button and blast the lock
            gothons can't get out. now that the bomb
            you run to the escape pod to get off this
            """))
            return 'escape_pod'

        else:

            print("does not complete!")
            return 'the_bridge'




class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        you rush through the ship desperately trying
        the escape pod before the whole ship explodes
        like hardly any gothons are on the ship, so you
        clear of interference. you get to the chamber escape
        pods, and now need to pick one to take them could be damaged
        but you don't have time. there's 5 pods, which one do you take?
        """))

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(dedent(f"""
            you jump into pod {guess} and hit the eject button.
            the pod escapes out into the void of space implodes as
            the hull ruptures,crushing you, jam jelly.
            """))
            return 'death'
        else:
            print(dedent(f"""
            you jump into pod {guess} and hit the eject button.
            the pod easily slides out into space head
            planet below. as it flies to the planet,back and see
            your ship implode then explo bright star, taking out the gothon
            ship a time. you won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("you won! good job!.")
        return 'finished'

class Map(object):

    scenes = {
    'central_corridor':CentralCorridor(),
    'laser_weapon_armory':LaserWeaponArmory(),
    'the_bridge':TheBridge(),
    'escape_pod':EscapePod(),
    'death':Death(),
    'finished':Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()





def main():
    pass

if __name__ == '__main__':
    main()