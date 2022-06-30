__init__ = "__main__"
__version__ = "1.0"
# Did you like the test ?
test = False
def start_scene():
    running = True
    text = font.render("Hi this is a test dialogue, please continue by mouse click", True, white)
    while running:
        screen.draw.fill((0, 128, 255))
        screen.draw.blit(char, (200, 0))
        textbox = pygame.draw.rect(screen.draw, (50, 50, 50, 200), (0, 430, 800, 150))
        screen.draw.blit(text, (20, 430))
        pygame.display.update()
        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            return
        elif pygame.event.get(pygame.QUIT):
            running = False
            endgame()
    pygame.quit()
            
def end_scene():
    running = True
    test = True
    text = font.render("I hope you will did a best game!", True, white)
    while running:
        screen.draw.fill((0, 128, 255))
        screen.draw.blit(char, (200, 0))
        textbox = pygame.draw.rect(screen.draw, (50, 50, 50, 200), (0, 430, 800, 150))
        screen.draw.blit(text, (20, 430))
        pygame.display.update()
        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            return
        elif pygame.event.get(pygame.QUIT):
            running = False
            endgame()
    pygame.quit()

if __init__ == "__main__":
    print("Welcome to a kinectic novel test.")
    print("Loading pygame_sdl2...")
    print("Starting game...")
    print("PyGame Main Menu Version", __version__)
    print("Completed loading starting scene.")
    start_scene()
    print("Completed loading ending scene.")
    end_scene()
