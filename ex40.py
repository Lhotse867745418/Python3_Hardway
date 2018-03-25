#-------------------------------------------------------------------------------
# Name:        modules, classed and objects
# Purpose:
#
# Author:      lhotse
#
# Created:     24/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you", "i don't want to get sued", "So i'll stop right there"])

bulls_on_parade = Song(["They really around the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

bulls_on_parade

def main():
    pass

if __name__ == '__main__':
    main()
