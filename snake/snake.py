import pygame


class Snake:
    """A class to represent a snake."""

    def __init__(self, screen):
        """Initialize class attributes."""
        self.screen = screen
        self.image = pygame.image.load(
            "snake/assets/images/snake.jpg"
        ).convert()
        self.direction = "right"  # Starting direction.
        self.length = 1
        self.x = [40]
        self.y = [40]
        self.speed = 0.15

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
        # Move snake body.
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Move snake head.
        if self.direction == "left":
            self.x[0] -= 40
        if self.direction == "right":
            self.x[0] += 40
        if self.direction == "up":
            self.y[0] -= 40
        if self.direction == "down":
            self.y[0] += 40

        self.draw()

    def draw(self):
        """Display snake on screen."""
        rgb = (0, 0, 0)
        self.screen.fill(rgb)
        for i in range(self.length):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        """Increase snake body size incrementally."""
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def increase_speed(self):
        """Increase snake speed incrementally."""
        self.speed -= 0.001
