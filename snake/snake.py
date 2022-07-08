import pygame


class Snake:
    """A class to represent a snake."""

    def __init__(self, screen):
        """Initialize class attributes."""
        self.screen = screen
        self.image = pygame.image.load("assets/snake.jpg").convert()
        self.direction = "right"  # Starting direction.
        self.x = 600
        self.y = 320

    def move_left(self):
        """Move snake left."""
        self.direction = "left"

    def move_right(self):
        """Move snake right."""
        self.direction = "right"

    def move_up(self):
        """Move snake up."""
        self.direction = "up"

    def move_down(self):
        """Move snake down."""
        self.direction = "down"

    def walk(self):
        """Move snake at constant speed and direction."""
        if self.direction == "left":
            self.x -= 40
        if self.direction == "right":
            self.x += 40
        if self.direction == "up":
            self.y -= 40
        if self.direction == "down":
            self.y += 40

        self.draw()

    def draw(self):
        """Display snake."""
        rgb = (0, 0, 0)
        self.screen.fill(rgb)
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
