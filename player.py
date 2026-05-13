import pygame

from bullet import Bullet
from helpers import load_frames, flip_frames, handle_portal_collision, advance_frame, apply_motion
from settings import vector

RUN_FRAMES = [f"Run ({i}).png" for i in range(1, 11)]
IDLE_FRAMES = [f"Idle ({i}).png" for i in range(1, 11)]
JUMP_FRAMES = [f"Jump ({i}).png" for i in range(1, 11)]
ATTACK_FRAMES = [f"Attack ({i}).png" for i in range(1, 11)]


class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()

        #Set constant variables
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8 #Gravity
        self.VERTICAL_JUMP_SPEED = 18 #Determines how high the player can jump
        self.STARTING_HEALTH = 100

        #Animation frames
        self.move_right_sprites = load_frames("images/player/run", RUN_FRAMES, (64, 64))
        self.move_left_sprites = flip_frames(self.move_right_sprites)

        self.idle_right_sprites = load_frames("images/player/idle", IDLE_FRAMES, (64, 64))
        self.idle_left_sprites = flip_frames(self.idle_right_sprites)

        self.jump_right_sprites = load_frames("images/player/jump", JUMP_FRAMES, (64, 64))
        self.jump_left_sprites = flip_frames(self.jump_right_sprites)

        self.attack_right_sprites = load_frames("images/player/attack", ATTACK_FRAMES, (64, 64))
        self.attack_left_sprites = flip_frames(self.attack_right_sprites)

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        #Animation booleans
        self.animate_jump = False
        self.animate_fire = False

        #Load sounds
        self.jump_sound = pygame.mixer.Sound("sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/player_hit.wav")

        #Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y


    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()

        #Update the player's mask
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """Move the player"""
        # Set the acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        # If the user is pressing a key, set the x-component of the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .5)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .5)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .5)
            else:
                self.animate(self.idle_left_sprites, .5)

        # Apply friction before integrating
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION

        apply_motion(self)


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between player and platforms when moving vertically
        if self.velocity.y != 0:
            collided_platforms = pygame.sprite.spritecollide(
                self, self.platform_group, False, pygame.sprite.collide_mask
            )
            if collided_platforms:
                if self.velocity.y > 0:
                    #Landing on a platform
                    self.position.y = collided_platforms[0].rect.top + 5
                    self.velocity.y = 0
                else:
                    #Hitting a platform from below while jumping
                    self.velocity.y = 0
                    while pygame.sprite.spritecollide(self, self.platform_group, False):
                        self.position.y += 1
                        self.rect.bottomleft = self.position

        # Collision check for portals
        handle_portal_collision(self)


    def check_animations(self):
        """Check to see if jump/fire animations should run"""
        #Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .1)
            else:
                self.animate(self.jump_left_sprites, .1)

        #Animate the player attack
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .25)
            else:
                self.animate(self.attack_left_sprites, .25)


    # noinspection PyTypeChecker
    def jump(self):
        """Jump upwards if on a platform"""
        #Only jump if on a platform
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self.jump_sound.play()
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
            self.animate_jump = True


    def fire(self):
        """Fire a 'bullet' from a sword"""
        self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True


    def reset(self):
        """Reset the player's position"""
        self.velocity = vector(0, 0)
        self.position = vector(self.starting_x, self.starting_y)
        self.rect.bottomleft = self.position

    def animate(self, sprite_list, speed):
        """Animate the player's actions"""
        self.current_sprite, wrapped = advance_frame(self.current_sprite, sprite_list, speed)
        if wrapped:
            if self.animate_jump:
                self.animate_jump = False
            if self.animate_fire:
                self.animate_fire = False
        self.image = sprite_list[int(self.current_sprite)]