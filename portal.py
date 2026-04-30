import random

import pygame

from helpers import load_frames

PORTAL_FRAMES = [f"tile{i:03d}.png" for i in range(22)]


class Portal(pygame.sprite.Sprite):
    """A class that if collided with will transport you"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        folder = None
        # TODO: if color == "green":
            # TODO: folder = "images/portals/green
        # TODO: else:
            # TODO: folder = "images/portals/purple"

        # TODO: assign load_frames() to self.portal sprites with these 3 arguments
        #  1: folder
        #  2: PORTAL_FRAMES
        #  3: (72, 72)

        #Load an image and get a rect
        # TODO: assign random.randint() to self.current_sprite with these 2 arguments
        #  1: 0
        #  2: len(self.portal_sprites) - 1

        # TODO: assign self.portal_sprites[self.current_sprite] to self.image
        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (x, y) to self.rect.bottomleft

        #Add to the portal group
        # TODO: call portal_group.add() with this 1 argument
        #  1: self

    def update(self):
        """Update the portal"""
        # TODO: call self.animate() pasing in these 2 arguments
        #  1: self.portal_sprites
        #  2: 0.2

    def animate(self, sprite_list, speed):
        """Animate the portal"""
        # TODO: if self.current_sprite < len(sprite_list) - 1:
            # TODO: add speed to self.current_sprite
        # TODO: else:
            # TODO: assign 0 to self.current_sprite

        # TODO: assign sprite_list[int(self.current_sprite)] to self.image
