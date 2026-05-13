import random

import pygame

from helpers import load_frames

PORTAL_FRAMES = [f"tile{i:03d}.png" for i in range(22)]


class Portal(pygame.sprite.Sprite):
    """A class that if collided with will transport you"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        if color == "green":
            folder = "images/portals/green"
        else:
            folder = "images/portals/purple"
        self.portal_sprites = load_frames(folder, PORTAL_FRAMES, (72, 72))

        #Load an image and get a rect
        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Add to the portal group
        portal_group.add(self)


    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, .2)


    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]