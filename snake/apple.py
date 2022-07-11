import pygame

from random import randint


class Apple:
    """A class to represent an apple."""

    def __init__(self, screen):
        """Initialize class attributes."""
        self.screen = screen
        self.image = pygame.image.load("snake/assets/apple.jpg").convert()
        self.x = 600
        self.y = 320

    def draw(self):
        """Display the apple."""
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        """Move the apple to random position."""
        self.x = randint(10, 15) * 40
        self.y = randint(10, 15) * 40
