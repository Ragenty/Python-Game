# Imports
import pygame
import sys

# Constants
WINDOW_WIDTH = 1320
WINDOW_HEIGHT = 780

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
<<<<<<< HEAD

=======
            
>>>>>>> 981c21cc258f4212bfa2ab18a1b343b5256c8314
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
