import pygame
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

# Load and transform the background image
background_image = pygame.transform.scale(
    pygame.image.load("bg.jpg"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load font
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))

        pygame.draw.rect(
            self.image,
            color,
            pygame.Rect(0, 0, width, height)
        )

        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):

        self.rect.x = max(
            min(
                self.rect.x + x_change,
                SCREEN_WIDTH - self.rect.width
            ),
            0
        )

        self.rect.y = max(
            min(
                self.rect.y + y_change,
                SCREEN_HEIGHT - self.rect.height
            ),
            0
        )


# Setup
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Collect All Sprites")

all_sprites = pygame.sprite.Group()

# Create player sprite
sprite1 = Sprite(pygame.Color('black'), 20, 30)

sprite1.rect.x = random.randint(
    0,
    SCREEN_WIDTH - sprite1.rect.width
)

sprite1.rect.y = random.randint(
    0,
    SCREEN_HEIGHT - sprite1.rect.height
)

all_sprites.add(sprite1)

# Create target sprites
targets = []

colors = [
    pygame.Color('red'),
    pygame.Color('yellow'),
    pygame.Color('green'),
    pygame.Color('blue')
]

for color in colors:

    target = Sprite(color, 20, 30)

    target.rect.x = random.randint(
        0,
        SCREEN_WIDTH - target.rect.width
    )

    target.rect.y = random.randint(
        0,
        SCREEN_HEIGHT - target.rect.height
    )

    all_sprites.add(target)

    targets.append(target)

# Game loop variables
running = True
won = False

clock = pygame.time.Clock()

# Main game loop
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                running = False

    if not won:

        keys = pygame.key.get_pressed()

        x_change = (
            keys[pygame.K_RIGHT] -
            keys[pygame.K_LEFT]
        ) * MOVEMENT_SPEED

        y_change = (
            keys[pygame.K_DOWN] -
            keys[pygame.K_UP]
        ) * MOVEMENT_SPEED

        sprite1.move(x_change, y_change)

        # Check collision with all targets
        for target in targets[:]:

            if sprite1.rect.colliderect(target.rect):

                all_sprites.remove(target)

                targets.remove(target)

        # Win condition
        if len(targets) == 0:
            won = True

    # Drawing
    screen.blit(background_image, (0, 0))

    all_sprites.draw(screen)

    # Display win message
    if won:

        win_text = font.render(
            "You Win!",
            True,
            pygame.Color('black')
        )

        screen.blit(
            win_text,
            (
                (SCREEN_WIDTH - win_text.get_width()) // 2,
                (SCREEN_HEIGHT - win_text.get_height()) // 2
            )
        )

    pygame.display.flip()

    clock.tick(90)

pygame.quit()