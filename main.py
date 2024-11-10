# Imports
import pygame
import sys

# Constants
INITIAL_WINDOW_WIDTH = 1320
INITIAL_WINDOW_HEIGHT = 780
FLOOR_HEIGHT_RATIO = 0.06  # Ratio of the floor height relative to the window height
BROWN = (139, 69, 19)
BEIGE = (237, 232, 208)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game")

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the window when clicking the "X"
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resize
            # Update the window size
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
    # Update window dimensions
    window_width, window_height = screen.get_size()
    floor_height = int(window_height * FLOOR_HEIGHT_RATIO)
    floor_y_position = window_height - floor_height

    # Clear screen and draw floor
    screen.fill(BEIGE)
    pygame.draw.rect(screen, BROWN, (0, floor_y_position, window_width, floor_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
