import random

import pygame

from helpers import load_frames, flip_frames, handle_portal_collision, apply_motion
from settings import WINDOW_WIDTH, vector, FPS

WALK_FRAMES = [f"Walk ({i}).png" for i in range(1, 11)]
DEAD_FRAMES = [f"Dead ({i}).png" for i in range(1, 11)]


class Zombie(pygame.sprite.Sprite):
    """An enemy class that moves across the screen"""

    def __init__(self, platform_group, portal_group, min_speed, max_speed):
        """Initialize the zombie"""
        super().__init__()

        #Set constant variables
        # Gravity
        # TODO: assign 3 to self.VERTICAL_ACCELERATION
        # TODO: assign 2 to self.RISE_TIME

        #Pick a gender and set the base folder
        folder = None
        # TODO: assign random.randint(0, 1) to gender
        # TODO: if gender == 0:
            # TODO: assign "images/zombie/boy" to folder
        # TODO: else:
            # TODO: assign "images/zombie/girl" to folder

        #Animation frames
        # TODO: assign load_frames() to self.walk_right_sprites with these 3 arguments
        #  1: f"{folder}/walk"
        #  2: WALK_FRAMES
        #  3: (64, 64)

        # TODO: assign flip_frames() to self.walk_left_sprites with this 1 arguments
        #  1: self.walk_right_sprites


        # TODO: assign load_frames() to self.die_right_sprites with these 3 arguments
        #  1: f"{folder}/dead"
        #  2: DEAD_FRAMES
        #  3: (64, 64)

        # TODO: assign flip_frames() to self.die_left_sprites with this 1 argument
        #  1: self.die_right_sprites

        #Rise is just death played in reverse — same frames, no need to reload
        # TODO: assign list(reversed(self.die_right_sprites)) to self.rise_right_sprites
        # TODO: assign list(reversed(self.die_left_sprites)) to self.rise_left_sprites

        #Load an image and get rect
        # TODO: assign random.choice([-1, 1]) to self.direction

        # TODO: assign 0 to self.current_sprite
        self.image = None
        # TODO: if self.direction == -1:
            # TODO: assign self.walk_left_sprites[self.current_sprite] to self.image
        # TODO: else:
            # TODO: assign self.walk_right_sprites[self.current_sprite] to self.image

        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (random.randint(100, WINDOW_WIDTH - 100), -100) to self.rect.bottomleft

        #Attach sprite groups
        # TODO: assign platform_group to self.platform_group
        # TODO: assign portal_group to self.portal_group

        #Animation booleans
        # TODO: assign False to self.animate_death
        # TODO: assign False to self.animate_rise

        #Load sounds
        # TODO: assign pygame.mixer.Sound("sounds/zombie_hit.wav") to self.hit_sound
        # TODO: assign pygame.mixer.Sound("sounds/zombie_kick.wav") to self.kick_sound
        # TODO: assign pygame.mixer.Sound("sounds/portal_sound.wav") to self.portal_sound

        #Kinematics vectors
        # TODO: assign vector() to self.position with these 2 arguments
        #  1: self.rect.x
        #  2: self.rect.y

        # TODO: assign vector() to self.velocity with these 2 arguments
        #  1: self.direction*random.randint(min_speed, max_speed)
        #  2: 0

        # TODO: assign vector() to self.acceleration with these 2 arguments
        #  1: 0
        #  2: self.VERTICAL_ACCELERATION

        #Initial zombie values
        # TODO: assign False to self.is_dead
        # TODO: assign 0 to self.round_time
        # TODO: assign 0 to self.frame_count

    def update(self):
        """Update the zombie"""
        # TODO: call self.move()
        # TODO: call self.check_collisions()
        # TODO: call self.check_animations()

        #Determine when the zombie should rise from the dead
        #TODO: if self.is_dead:
            # TODO: add 1 to self.frame_count
            # TODO: if self.frame_count % FPS == 0:
                # TODO: add 1 to self.round_time
                # TODO: if self.round_time == self.RISE_TIME:
                    # TODO: assign True to self.animate_rise
                    #When the zombie died, the image was kept as the last image
                    #When it rises, we want to start at index 0 of our rise_sprite lists
                    # TODO: assign 0 to self.current_sprite

    def move(self):
        """Move the zombie"""
        # TODO: if not self.is_dead:
            # TODO: if self.direction == -1:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.walk_left_sprites
                #  2: 0.5
            # TODO: else:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.walk_right_sprites
                #  2: 0.5

            # TODO: call apply_motion() with 1 argument
            #  1: self


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between zombie and platforms when falling
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


    def check_animations(self):
        """Check to see if death/rise animations should run"""
        #Animate the zombie death
        # TODO: if self.animate_death:
            # TODO: if self.direction == 1:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.die_right_sprites
                #  2: 0.095
            # TOD: else:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.die_left_sprites
                #  2: 0.095

        #Animate the zombie rise
        # TODO: if self.animate_rise:
            # TODO: if self.direction == 1:
                # TODO: call self.animate()
                #  1: self.rise_right_sprites
                #  2:  0.095
            # TODO: else:
                # TODO: call self.animate()
                #  1: self.rise_left_sprites
                #  2:  0.095


    def animate(self, sprite_list, speed):
        """Animate the zombie's actions"""
        # TODO: if self.current_sprite < len(sprite_list) -1:
            # TODO: add speed to self.current_sprite
        # TODO: else:
            # TODO: assign 0 to self.current_sprite
            #End the death animation
            # TODO: if self.animate_death:
                # TODO: assign len(sprite_list) - 1 to self.current_sprite = len(sprite_list)
                # TODO: assign False to self.animate_death
            #End the rise animation
            # TODO: if self.animate_rise:
                # TODO: assign False to self.animate_rise
                # TODO: assign False to self.is_dead
                # TODO: assign 0 to self.frame_count
                # TODO: assign 0 to self.round_time

        # TODO: assign sprite_list[int(self.current_sprite)] to self.image