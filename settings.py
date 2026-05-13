import pygame

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
FPS = 60

vector = pygame.math.Vector2

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

clock = pygame.time.Clock()