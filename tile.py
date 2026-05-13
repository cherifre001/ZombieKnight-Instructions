import pygame


class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=None):
        """Initialize the tile"""
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load(f"images/tiles/Tile ({image_int}).png"),
            (32, 32),
        )

        if sub_group is not None:
            sub_group.add(self)
        main_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)