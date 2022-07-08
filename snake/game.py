import pygame

from pygame.locals import *
from snake import Snake


class Game:
    """A class to represent a snake game."""

    def __init__(self):
        """Initialize class attributes."""
        pygame.init()
        pygame.display.set_caption("Snake")
        self.surface = pygame.display.set_mode((1280, 720))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def start_game(self):
        """Start the game."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Quit game.
                    if event.key == K_ESCAPE:
                        running = False

                    # Move snake around.
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False
