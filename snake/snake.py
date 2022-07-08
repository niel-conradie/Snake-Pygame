import pygame

from pygame.locals import *


def draw_snake():
    """Display snake."""
    rgb = (0, 0, 0)
    surface.fill(rgb)
    surface.blit(snake, (snake_x, snake_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    # Display screen.
    pygame.display.set_caption("Snake")
    surface = pygame.display.set_mode((1280, 720))
    rgb = (0, 0, 0)
    surface.fill(rgb)

    # Import snake image.
    snake = pygame.image.load("snake/assets/snake.jpg").convert()
    snake_x, snake_y = 600, 320
    surface.blit(snake, (snake_x, snake_y))
    pygame.display.flip()

    # Move snake conditions.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Quit game.
                if event.key == K_ESCAPE:
                    running = False

                # Move snake around.
                if event.key == K_LEFT:
                    snake_x -= 40
                    draw_snake()
                if event.key == K_RIGHT:
                    snake_x += 40
                    draw_snake()
                if event.key == K_UP:
                    snake_y -= 40
                    draw_snake()
                if event.key == K_DOWN:
                    snake_y += 40
                    draw_snake()

            elif event.type == QUIT:
                running = False
