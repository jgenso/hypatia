"""Entities: interactive/dynamic map objects.
Lillian Lynn Mahoney <lillian.lynn.mahoney@gmail.com>
2014-10-20

Different kinds of entities, namely:
  * Walkabout()

"""


import os
import glob
import render
import pyganim
from collections import OrderedDict


__author__ = "Lillian Lynn Mahoney"
__copyright__ = "Copyright 2014, Lillian Lynn Mahoney"
__credits__ = ["Lillian Mahoney"]
__license__ = "Attribution Assurance License"
__version__ = "0.1"
__maintainer__ = "Lillian Mahoney"
__email__ = "lillian.lynn.mahoney@gmail.com"
__status__ = "Development"


class Player(object):

    def __init__(self, walkabout=None):
        """NPC or human player; depends on which controller
        is assigned.

        Args:
          walkabout (Walkabout): walkabout settings/sprites

        """

        self.walkabout = walkabout or Walkabout('debug')


class Walkabout(object):

    def __init__(self, walkabout_directory, start_position=None, speed=1):
        """Interactive entity which uses a walkabout sprite.

        An entity capable of walking about the map. Sprites for
        "walking about" are defined as action__direction.gif therein
        the specified walkabout_directory.

        ASSUMPTION: walkabout_directory contains sprites for
        walk, run actions.

        Args:
          walkabout_directory (str): directory containing (animated)
            walkabout GIFs. Assumed parent is data/walkabouts/
          start_position (tuple): (x, y) coordinates (integers)
            referring to absolute pixel coordinate.
          speed (int): the number of pixels moved per update/frame.

        Unfinished:
          * Anchors: head, hands, feet, torso

        """

        walkabout_directory = os.path.join('data', 'walkabouts',
                                           walkabout_directory)
        sprite_name_pattern = os.path.join(walkabout_directory, '*.gif')
        self.sprites = {}

        for sprite_path in glob.iglob(sprite_name_pattern):
            file_name, file_ext = os.path.splitext(sprite_path)
            file_name = os.path.split(file_name)[1]
            action, direction = file_name.split('_', 1)
            animation = render.gif_to_pyganim(sprite_path)
            animation.convert()
            animation.play()

            try:
                self.sprites[action][direction] = animation
            except KeyError:
                self.sprites[action] = {direction: animation}

        self.action = 'stand'
        self.direction = 'up'
        self.position = start_position or (0, 0)  # px values
        self.speed = 20  # one pixel per update

    def move(self, direction):
        """

        Args:
          direction (str): may be one of: up, right, down, left

        """

        self.direction = direction
        self.action = 'walk'
        x, y = self.position

        if direction == 'up':
            y -= self.speed
        elif direction == 'right':
            x += self.speed
        elif direction == 'down':
            y += self.speed
        elif direction == 'left':
            x -= self.speed

        self.position = (x, y)

    def blit(self, screen):
        """Draw the appropriate/active animation to screen.

        Args:
          screen (pygame.Surface): the primary display/screen.

        Returns:
          None

        """

        self.sprites[self.action][self.direction].blit(screen, self.position)

        return None


def walkabout_generator():
    """Create the walkabout sprites for a character
    based off of some info.

    Gender, obvs.

    Why not make this a meta class?

    """

    pass
