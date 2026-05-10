import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# create a window
screen = pygame.display.set_mode([800, 600])

# load a background image
background = pygame.image.load(os.path.join('assets', 'background.png'))
background = pygame.transform.scale(background, screen.get_size())
running = True

while running:
    # Background color
    screen.fill((255, 255, 255))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
