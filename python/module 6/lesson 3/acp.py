# Create a group to hold the sprites
all_sprites_list = pygame.sprite.Group()

# Create 5 sprites
for i in range(5):
    sprite = Sprite(WHITE, 20, 30)
    sprite.rect.x = random.randint(0, 480)
    sprite.rect.y = random.randint(0, 370)

    all_sprites_list.add(sprite)