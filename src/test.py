import pygame
import sys
import os


class Button:
    def __init__(self, text, width, height, pos):
        # top rectangle
        self.top_rect = pygame.Rect((pos), (width, height))
        self.top_color = "#475F77" 

        # text
        self.text_surf = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            print("overlap)")

# Initialize Pygame
pygame.init()

# screen resolution
res = (800, 600)

# create a window
screen = pygame.display.set_mode(res)

# set window title
pygame.display.set_caption("My Game")

# set up the clock for a decent framerate
clock = pygame.time.Clock()

# Font for gmae
font = pygame.font.SysFont(None, 36)

# store height and width for later
width = screen.get_width()
height = screen.get_height()

# load a background image
background = pygame.image.load(os.path.join('assets', 'background.png'))
background = pygame.transform.scale(background, screen.get_size())

button1 = Button("Play", 200, 50, ((width // 2)-100, (height // 2)-25))


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    screen.fill((255, 255, 255))
    # Background image
    screen.blit(background, (0, 0))

    
    button1.draw()
    
    pygame.display.flip()

pygame.quit()
