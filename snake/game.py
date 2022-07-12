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

    def display_score(self):
        """Display the score."""
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length - 1}", True, (255, 255, 255))
        self.surface.blit(score, (1125, 10))

    def game_over(self):
        """Display game over on screen."""
        rgb = (0, 0, 0)
        self.surface.fill(rgb)
        # Display game over on screen.
        game_over_font = pygame.font.SysFont("arial", 50)
        game_over = game_over_font.render("GAME OVER!", True, (255, 255, 255))
        self.surface.blit(game_over, (475, 275))
        # Display score on screen.
        score_font = pygame.font.SysFont("arial", 35)
        score = score_font.render(
            f"SCORE: {self.snake.length - 1}", True, (255, 255, 255)
        )
        self.surface.blit(score, (550, 350))
        # Display restart on screen.
        restart_font = pygame.font.SysFont("arial", 30)
        restart = restart_font.render(
            "To play again press Enter! To exit press Escape!", True, (255, 255, 255)
        )
        self.surface.blit(restart, (300, 600))

        pygame.display.flip()

    def reset(self):
        """Reset snake and apple to default position."""
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def play(self):
        """Play the game."""
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Collision with apple condition.
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.snake.increase_speed()
            self.apple.move()

        # Collision with snake condition.
        for i in range(2, self.snake.length):
            if self.collision(
                self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]
            ):
                raise TypeError

        # Collision with border condition.
        if not (0 <= self.snake.x[0] <= 1240 and 0 <= self.snake.y[0] <= 680):
            raise TypeError

    def start_game(self):
        """Start the game."""
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Quit game.
                    if event.key == K_ESCAPE:
                        running = False
                    # Pause game.
                    if event.key == K_RETURN:
                        pause = False

                    # Change snake direction.
                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except TypeError:
                self.game_over()
                pause = True
                self.reset()

            # Update snake position interval.
            sleep(self.snake.speed)
