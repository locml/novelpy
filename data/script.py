# Did you like the test ?
test = False
def start_scene():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    char = Character()
    all_sprites.add(char)
    running = True
    text = font.render("Hi this is a test dialogue, please continue by click to the screen.", True, WHITE)
    while running:
        screen.fill((0, 128, 255))
        textbox = pygame.draw.rect(screen, (50, 50, 50, 200), (0, 430, 800, 150))
        all_sprites.draw(screen)
        screen.blit(text, (20, 430))
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
    
def second_scene():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    char = Character()
    all_sprites.add(char)
    running = True
    narrator = font.render("Example Name", True, GREEN)
    text = font.render("This is another dialogue for this example contains name too!", True, WHITE)
    while running:
        screen.fill((0, 128, 255))
        textbox = pygame.draw.rect(screen, (50, 50, 50, 200), (0, 430, 800, 150))
        all_sprites.draw(screen)
        screen.blit(narrator, (20, 430))
        screen.blit(text, (20, 460))
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
    
def end_scene():
    pygame.init()
    running = True
    test = True
    text = font.render("I hope you will did a best game!", True, WHITE)
    all_sprites = pygame.sprite.Group()
    char = Character()
    char.image = char.images[1]
    char.image.set_colorkey(WHITE)   
    all_sprites.add(char)
    while running:
        screen.fill((0, 128, 255))
        textbox = pygame.draw.rect(screen, (50, 50, 50, 200), (0, 430, 800, 150))
        all_sprites.draw(screen)
        screen.blit(text, (20, 430))
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
start_scene()
second_scene()
end_scene()
