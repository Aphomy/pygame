import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Display Text')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 48)

# Render the text
text = font.render('Hello, Pygame!', True, BLACK)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Blit the text onto the screen
    screen.blit(text, (300, 250))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
