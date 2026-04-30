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
        # Gravity
        # TODO: assign 3 to self.VERTICAL_ACCELERATION
        # TODO: assign 5 to self.HORIZONTAL_VELOCITY

        #Animation frames
        # TODO: assign load_frames() to self.ruby_sprites with these 3 arguments
        #  1: "images/ruby"
        #  2: RUBY_FRAMES
        #  3: (64, 64)

        #Load image and get rect
        # TODO: assign 0 to self.current_sprite
        # TODO: assign self.ruby_sprites[self.current_sprite] to self.image
        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (WINDOW_WIDTH // 2, 100) to self.rect.bottomleft


        #Attach sprite groups
        # TODO: assign platform_group to self.platform_group
        # TODO: assign portal_group to self.portal_group

        #Load sounds
        # TODO: assign pygame.mixer.Sound() to self.portal_sound with this 1 argument
        # 1: "sounds/portal_sound.wav"

        #Kinematic vectors
        # TODO: assign vector() to self.position with these 2 arguments
        #  1: self.rect.x
        #  2: self.rect.y

        # TODO: assign vector() to self.velocity with these 2 arguments
        #  1: random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY])
        #  2: 0

        # TODO: assign vector() to self.acceleration with these 2 arguments
        #  1: 0
        #  2: self.VERTICAL_ACCELERATION


    def update(self):
        """Update the ruby"""
        # TODO: call self.animate() with these 2 arguments
        #  1: self.ruby_sprites
        #  2: 0.25

        # TODO: call self.move()
        # TODO: call self.check_collisions()


    def move(self):
        """Move the ruby"""
        # TODO: call apply_motion() with 1 argument
        #  1: self


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        # TODO: assign pygame.sprite.spritecollide() to collided_platforms with these 3 arguments
        #  1: self
        #  2: self.platform_group
        #  3: False

        # TODO: if collided_platforms:
            # TODO: assign collided_platforms[0].rect.top + 1 to self.position.y
            # TODO: assign 0 to self.velocity.y

        # Collision check for portals
        # TODO: call handle_portal_collision() with 1 argument
        #  1: self


    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        # TODO: if self.current_sprite < len(sprite_list) -1:
            # TODO: add speed to self.current_sprite
        # TODO: else:
            # TODO: assign 0 to self.current_sprite
        # TODO: assign sprite_list[int(self.current_sprite)] to self.image
