# pyright: reportMissingImports=false
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

while not done:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw a rectangle
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    # Draw a circle
    pygame.draw.circle(screen, (255, 0, 0), (200, 80), 40)

    # Draw a line
    pygame.draw.line(screen, (0, 255, 0), (50, 200), (300, 200), 5)

    pygame.display.flip()

pygame.quit()