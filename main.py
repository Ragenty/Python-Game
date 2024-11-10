# Imports
import pygame
import sys
import math

# Constants
INITIAL_WINDOW_WIDTH = 1320
INITIAL_WINDOW_HEIGHT = 780
FLOOR_HEIGHT_RATIO = 0.06  # Ratio of the floor height relative to the window height
BROWN = (139, 69, 19)
BEIGE = (237, 232, 208)
RED = (255, 0, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
JUMP_HEIGHT = PLAYER_HEIGHT * 3  # Desired jump height (3 times player height)
MOVE_SPEED = 3.75  # Reduced movement speed for 25% slower horizontal movement

# Set gravity to make the player fall 0.5 of their height per second
GRAVITY = 0.05 * PLAYER_HEIGHT  # Fall rate is 0.5 times the player height per second
JUMP_STRENGTH = math.sqrt(0.5 * GRAVITY * JUMP_HEIGHT)  # Calculate jump velocity

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game")

# Player variables
player_x = INITIAL_WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = INITIAL_WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2
velocity_y = 0
velocity_x = 0
on_floor = False  # Boolean to check if player is on the floor

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
        elif event.type == pygame.KEYDOWN:
            # Jump with space, up arrow, or W if on the floor
            if (event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP) and on_floor:
                velocity_y = -JUMP_STRENGTH  # Negative for upward jump
                on_floor = False  # The player is now in the air

    # Handle continuous key presses for side-to-side movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Move left
        velocity_x = -MOVE_SPEED
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
        velocity_x = MOVE_SPEED
    else:
        velocity_x = 0  # Stop horizontal movement when no key is pressed

    # Update window dimensions
    window_width, window_height = screen.get_size()
    floor_height = int(window_height * FLOOR_HEIGHT_RATIO)
    floor_y_position = window_height - floor_height

    # Apply gravity (falling speed increases)
    velocity_y += GRAVITY  # Update velocity due to gravity
    player_y += velocity_y  # Apply vertical movement to player

    # Apply horizontal movement
    player_x += velocity_x  # Move player left/right based on velocity

    # Prevent player from moving out of window bounds
    if player_x < 0:
        player_x = 0
    elif player_x + PLAYER_WIDTH > window_width:
        player_x = window_width - PLAYER_WIDTH

    # Check if the player hits the floor (ground collision detection)
    if player_y + PLAYER_HEIGHT >= floor_y_position:
        player_y = floor_y_position - PLAYER_HEIGHT  # Place player on the floor
        velocity_y = 0  # Stop falling
        on_floor = True  # Player is now on the floor

    # Clear screen and draw background
    screen.fill(BEIGE)
    
    # Draw floor
    pygame.draw.rect(screen, BROWN, (0, floor_y_position, window_width, floor_height))
    
    # Draw player rectangle in red
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
