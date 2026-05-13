import random

import pygame

from helpers import load_frames, handle_portal_collision, apply_motion, RUBY_FRAMES
from settings import WINDOW_WIDTH, vector


class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, platform_group, portal_group):
        """Initialize the ruby"""
        super().__init__()

        #Set constant variables
        self.VERTICAL_ACCELERATION = 3 #Gravity
        self.HORIZONTAL_VELOCITY = 5

        #Animation frames
        self.ruby_sprites = load_frames("images/ruby", RUBY_FRAMES, (64, 64))

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WINDOW_WIDTH//2, 100)

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        #Load sounds
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

        #Kinematic vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(random.choice([-1*self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)


    def update(self):
        """Update the ruby"""
        self.animate(self.ruby_sprites, .25)
        self.move()
        self.check_collisions()


    def move(self):
        """Move the ruby"""
        apply_motion(self)


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision check for portals
        handle_portal_collision(self)


    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]