import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT


RUBY_FRAMES = [f"tile00{i}.png" for i in range(7)]


def load_frames(folder, filenames, size):
    """Load and scale a list of sprite frames from a folder."""
    return [
        pygame.transform.scale(pygame.image.load(f"{folder}/{name}"), size)
        for name in filenames
    ]


def flip_frames(frames):
    """Return a list of horizontally-flipped copies of the given frames."""
    return [pygame.transform.flip(s, True, False) for s in frames]


def advance_frame(current, sprite_list, speed):
    """Advance an animation index, wrapping at the end.
    Returns (new_index, wrapped_bool) — wrapped is True the frame the cycle resets."""
    if current < len(sprite_list) - 1:
        return current + speed, False
    return 0, True


def teleport(sprite):
    """Move a sprite to the opposite portal exit and update its rect."""
    if sprite.position.x > WINDOW_WIDTH // 2:
        sprite.position.x = 86
    else:
        sprite.position.x = WINDOW_WIDTH - 150

    if sprite.position.y > WINDOW_HEIGHT // 2:
        sprite.position.y = 64
    else:
        sprite.position.y = WINDOW_HEIGHT - 132

    sprite.rect.bottomleft = sprite.position


def handle_portal_collision(sprite):
    """If sprite hit a portal, play its sound and teleport.
    Requires sprite to have .portal_group, .portal_sound, .position, .rect."""
    if pygame.sprite.spritecollide(sprite, sprite.portal_group, False):
        sprite.portal_sound.play()
        teleport(sprite)


def apply_motion(sprite):
    """Integrate kinematics, wrap horizontally, sync rect to position.
    Requires sprite to have .velocity, .acceleration, .position, .rect."""
    sprite.velocity += sprite.acceleration
    sprite.position += sprite.velocity + 0.5 * sprite.acceleration
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

            # Set constant variables
            self.VERTICAL_ACCELERATION = 3  # Gravity
            self.RISE_TIME = 2

            # Pick a gender and set the base folder
            gender = random.randint(0, 1)
            folder = "images/zombie/boy" if gender == 0 else "images/zombie/girl"

            # Animation frames
            self.walk_right_sprites = load_frames(f"{folder}/walk", WALK_FRAMES, (64, 64))
            self.walk_left_sprites = flip_frames(self.walk_right_sprites)

            self.die_right_sprites = load_frames(f"{folder}/dead", DEAD_FRAMES, (64, 64))
            self.die_left_sprites = flip_frames(self.die_right_sprites)

            # Rise is just death played in reverse — same frames, no need to reload
            self.rise_right_sprites = list(reversed(self.die_right_sprites))
            self.rise_left_sprites = list(reversed(self.die_left_sprites))

            # Load an image and get rect
            self.direction = random.choice([-1, 1])

            self.current_sprite = 0
            if self.direction == -1:
                self.image = self.walk_left_sprites[self.current_sprite]
            else:
                self.image = self.walk_right_sprites[self.current_sprite]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = (random.randint(100, WINDOW_WIDTH - 100), -100)

            # Attach sprite groups
            self.platform_group = platform_group
            self.portal_group = portal_group

            # Animation booleans
            self.animate_death = False
            self.animate_rise = False

            # Load sounds
            self.hit_sound = pygame.mixer.Sound("sounds/zombie_hit.wav")
            self.kick_sound = pygame.mixer.Sound("sounds/zombie_kick.wav")
            self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

            # Kinematics vectors
            self.position = vector(self.rect.x, self.rect.y)
            self.velocity = vector(self.direction * random.randint(min_speed, max_speed), 0)
            self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

            # Initial zombie values
            self.is_dead = False
            self.round_time = 0
            self.frame_count = 0

        def update(self):
            """Update the zombie"""
            self.move()
            self.check_collisions()
            self.check_animations()

            # Determine when the zombie should rise from the dead
            if self.is_dead:
                self.frame_count += 1
                if self.frame_count % FPS == 0:
                    self.round_time += 1
                    if self.round_time == self.RISE_TIME:
                        self.animate_rise = True
                        # When the zombie died, the image was kept as the last image
                        # When it rises, we want to start at index 0 of our rise_sprite lists
                        self.current_sprite = 0

        def move(self):
            """Move the zombie"""
            if not self.is_dead:
                if self.direction == -1:
                    self.animate(self.walk_left_sprites, .5)
                else:
                    self.animate(self.walk_right_sprites, .5)

                apply_motion(self)

        # noinspection PyTypeChecker
        def check_collisions(self):
            """Check for collisions with platforms and portals"""
            # Collision check between zombie and platforms when falling
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 1
                self.velocity.y = 0

            # Collision check for portals
            handle_portal_collision(self)

        def check_animations(self):
            """Check to see if death/rise animations should run"""
            # Animate the zombie death
            if self.animate_death:
                if self.direction == 1:
                    self.animate(self.die_right_sprites, .095)
                else:
                    self.animate(self.die_left_sprites, .095)

            # Animate the zombie rise
            if self.animate_rise:
                if self.direction == 1:
                    self.animate(self.rise_right_sprites, .095)
                else:
                    self.animate(self.rise_left_sprites, .095)

        def animate(self, sprite_list, speed):
            """Animate the zombie's actions"""
            if self.current_sprite < len(sprite_list) - 1:
                self.current_sprite += speed
            else:
                self.current_sprite = 0
                # End the death animation
                if self.animate_death:
                    self.current_sprite = len(sprite_list) - 1
                    self.animate_death = False
                # End the rise animation
                if self.animate_rise:
                    self.animate_rise = False
                    self.is_dead = False
                    self.frame_count = 0
                    self.round_time = 0

            self.image = sprite_list[int(self.current_sprite)]
    if sprite.position.x < 0:
        sprite.position.x = WINDOW_WIDTH
    elif sprite.position.x > WINDOW_WIDTH:
        sprite.position.x = 0

    sprite.rect.bottomleft = sprite.position