import pygame

from helpers import load_frames, RUBY_FRAMES


class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated.  A ruby will be generated here."""

    def __init__(self, x, y, main_group):
        """Initialize the ruby maker"""
        super().__init__()

        #Animation frames
        # TODO: assign load_frames() to self.ruby_sprites with 3 arguments
        #  1: "image/ruby"
        #  2: RUBY_FRAMES
        #  3: (64, 64)

        #Load image and get rect
        # TODO: assign 0 to self.current_sprite
        # TODO: assign self.ruby_sprites[self.current_sprite] to self.image
        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (x, y) to self.rect.bottomleft

        #Add to the main group for drawing purposes
        # TODO: call main_group.add() with this 1 argument
        #  1: self


    def update(self):
        """Update the ruby maker"""
        # TODO: call self.animate with 2 arguments
        #  1: self.ruby_sprites
        #  2: 0.25

    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        # TODO: if self.current_sprite < len(sprite_list) -1:
            # TODO: add speed to self.current_sprite
        # TODO: else:
            # TODO: assign 0 to self.current_sprite

        # TODO: assign sprite_list[int(self.current_sprite)] to self.image
