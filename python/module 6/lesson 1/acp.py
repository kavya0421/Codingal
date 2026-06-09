# Import Necessary Libraries
import pygame

# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((500, 400))

# Set window title
pygame.display.set_caption("My First Game Screen")

# Create a loop to run till the game is quit by the user
done = False

while not done:

    # Fill the screen with a color
    screen.fill((135, 206, 235))

    # Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Make the changes visible
    pygame.display.flip()

pygame.quit()