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
    # TODO: if current < len(sprite_list) - 1:
        # TODO: return current + speed, False
    # TODO: return 0, True


def teleport(sprite):
    """Move a sprite to the opposite portal exit and update its rect."""
    # TODO: if sprite.position.x > WINDOW_WIDTH // 2:
        # TODO: assign 86 to sprite.position.x
    # TODO: else:
        # TODO: assign WINDOW_WIDTH - 150 to sprite.position.x

    # TODO: if sprite.position.y > WINDOW_HEIGHT // 2:
        # TODO: assign 64 to sprite.position.y
    # TODO: else:
        # TODO: assign WINDOW_HEIGHT - 132 to sprite.position.y

    # TODO: assign sprite.position to sprite.rect.bottomleft


def handle_portal_collision(sprite):
    """If sprite hit a portal, play its sound and teleport.
    Requires sprite to have .portal_group, .portal_sound, .position, .rect."""
    # TODO: if pygame.sprite.spritecollide(sprite, sprite.portal_group, False):
        # TODO: call sprite.portal_sound.play()
        # TODO: call teleport() with 1 argument
        # 1: sprite


def apply_motion(sprite):
    """Integrate kinematics, wrap horizontally, sync rect to position.
    Requires sprite to have .velocity, .acceleration, .position, .rect."""
    # TODO: add sprite.accleration to sprite.velocity
    # TODO: add sprite.velocity + 0.5 * sprite.acceleration to sprite.position

    # TODO: if sprite.position.x < 0:
        # TODO: assign WINDOW_WIDTH to sprite.position.x
    # TODO: elif sprite.position.x > WINDOW_WIDTH:
        # TODO: assign 0 to sprite.position.x

    # TODO: assign sprite.position to sprite.rect.bottomleft