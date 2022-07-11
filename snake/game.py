import pygame

from pygame.locals import *
from time import sleep

from snake import Snake
from apple import Apple


class Game:
    """A class to represent a snake game."""

    def __init__(self):
        """Initialize class attributes."""
        pygame.init()
        pygame.display.set_caption("Snake")
        self.surface = pygame.display.set_mode((1280, 720))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    @staticmethod
    def collision(x1, y1, x2, y2):
        """Collision detection."""
        if x1 >= x2 and x1 < x2 + 40:
            if y1 >= y2 and y1 < y2 + 40:
                return True
        return False

    def play(self):
        """Play the game."""
        self.snake.walk()
        self.apple.draw()
        pygame.display.flip()

        # Collision with apple condition.
        if self.collision(self.snake.x, self.snake.y, self.apple.x, self.apple.y):
            self.apple.move()

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

            self.play()

            # Update snake position interval.
            sleep(0.15)
