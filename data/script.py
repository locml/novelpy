
# Did you like the test ?
test = False
def start_scene():
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
        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            return
        elif pygame.event.get(pygame.QUIT):
            running = False
            endgame()
    pygame.quit()
            
def end_scene():
    running = True
    test = True
    text = font.render("I hope you will did a best game! But this limited my word...", True, WHITE)
    all_sprites = pygame.sprite.Group()
    char = Character()
    char.image = char.images[1]
    char.image.set_colorkey(BLACK)   
    all_sprites.add(char)
    while running:
        screen.fill((0, 128, 255))
        textbox = pygame.draw.rect(screen, (50, 50, 50, 200), (0, 430, 800, 150))
        all_sprites.draw(screen)
        screen.blit(text, (20, 430))
        pygame.display.update()
        all_sprites.update()
        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            return
        elif pygame.event.get(pygame.QUIT):
            running = False
            endgame()
    pygame.quit()

print("Welcome to a kinectic novel test.")
print("Loading pygame_sdl2...")
print("Starting game...")
print("PyGame Visual Novel")
print("Completed loading starting scene.")
start_scene()
print("Completed loading ending scene.")
end_scene()
