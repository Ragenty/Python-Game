# Imports
import pygame
import sys
import math

# Constants
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 180

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)

pygame.display.set_caption("Game")

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the window when clicking the "X"
            running = False

    # Fill the screen with a color (e.g., white) to update continuously
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
