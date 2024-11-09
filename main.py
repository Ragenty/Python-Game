# Imports
import pygame
import sys

# Constants
WINDOW_WIDTH = 1320
WINDOW_HEIGHT = 780
floor_height = 50
floor_y_position = WINDOW_HEIGHT - floor_height
BROWN = (139, 69, 19)
BEIGE = (237,232,208)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game")

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the window when clicking the "X"
            running = False
            
    screen.fill(BEIGE)
    pygame.draw.rect(screen, BROWN, (0, floor_y_position -50, WINDOW_WIDTH, floor_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
