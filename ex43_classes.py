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

class Scene(object):
    def enter(selsf):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()





def main():
    pass

if __name__ == '__main__':
    main()
