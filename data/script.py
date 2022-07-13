test = False # Did you has ended the test ?
def start_scene():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    char = Character()
    textbox = Textbox(screen, (50, 50, 50), 0, 430, 1280, 300, 12)
    all_sprites.add(char)
    all_sprites.add(textbox)
    running = True
    while running:
        clock.tick(FPS)
        screen.fill((0, 128, 255))
        all_sprites.draw(screen)
        textbox.draw(screen, "Hi this is a test dialogue, please continue by click to the choice in screen.", 20, 430)
        if active_fps:
            fps_counter()
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return
    
def second_scene():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    char = Character()
    textbox = Textbox(screen, (50, 50, 50), 0, 430, 1280, 300, 12)
    all_sprites.add(char)
    all_sprites.add(textbox)
    running = True
    narrator = font.render("Example Name", True, GREEN)
    while running:
        clock.tick(FPS)
        screen.fill((0, 128, 255))
        all_sprites.draw(screen)
        textbox.draw(screen, "This is another dialogue for this example contains name too!", 20, 460)
        screen.blit(narrator, (20, 430))
        if active_fps:
            fps_counter()
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return
            
            
def end_scene():
    pygame.init()
    running = True
    test = True
    all_sprites = pygame.sprite.Group()
    char = Character()
    char.image = char.images[1]
    char.image.set_colorkey(WHITE)   
    textbox = Textbox(screen, (50, 50, 50, 150), 0, 430, 1280, 300, 12 )
    all_sprites.add(char)
    all_sprites.add(textbox)
    while running:
        clock.tick(FPS)
        screen.fill((0, 128, 255))
        all_sprites.draw(screen)
        textbox.draw(screen, "I hope you will did a best game! So boring when you had to go...", 20, 430)
        if active_fps:
            fps_counter()
        pygame.display.update()
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return
start_scene()
second_scene()
end_scene()
