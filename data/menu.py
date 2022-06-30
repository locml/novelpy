import pygame_sdl2 as pygame
pygame.init()
class _Screen:
    pass
white = pygame.Color("white")
dark_blue = pygame.Color("darkblue")
light_blue = (0, 128, 255, 255)
screen = _Screen()
mm_window = pygame.image.load("data/menu_bg.png")
char = pygame.image.load("data/character.png")
screen_width, screen_height, screen_flags, screen_depths, screen_caption  = 800, 600, 0, 32, "PyGame Main Menu"
screen.draw = pygame.display.set_mode((screen_width, screen_height), screen_flags, screen_depths)
screen.caption = pygame.display.set_caption(screen_caption)
font = pygame.sysfont.SysFont("dejavu-sans", 33)
st = font.render("Start Game", True, white)
at = font.render("About", True, white)
ht = font.render("Help", True, white)
qt = font.render("Quit Game", True, white)

def draw_rect(x, y, width, height):
    '''
    Method for draw rect easily without repeatdly
    write pygame.draw.rect()
    '''
    return pygame.draw.rect(screen.draw, light_blue, pygame.Rect((x, y), (width, height)))

def clicked_sound():
    '''
    Used for playing when clicking
    the rect in collidepoint.
    '''
    pygame.mixer.music.load("data/click.mp3")
    pygame.mixer.music.play()

def execfile(filename, globals=None, locals=None):
    # This method is recreating of execfile method in
    # Python 2 for executing file.
    '''
    This function is similar to the exec statement, but parses
    a file instead of a string. It is different from the
    import statement in that it does not use the module administration —it reads
    the file unconditionally and does not create a new module. 
    The arguments are a file name and two optional dictionaries. The file is parsed and evaluated as a sequence of
    Python statements (similarly to a module) using the globals and locals dictionaries as global and local namespace.
    If provided, locals can be any mapping object. Remember that at module level, globals and locals are the same dictionary.
    If two separate objects are passed as globals and locals, the code will be executed as if it were embedded in a class definition.
    If the locals dictionary is omitted it defaults to the globals dictionary.
    If both dictionaries are omitted, the expression is executed in the environment
    where execfile() is called. The return value is None.
    '''
    return exec(open(filename).read(), globals, locals)
def endgame():
    print("Uninitalizing pygame_sdl2 as pygame...")
    print("Uninitalizing pygame_sdl2...")
    print("Uninitalizing game...")
    pygame.quit()
    print("Uninitalized.")
running = True
while running:
    screen.draw.fill((0, 0, 0))
    screen.draw.blit(mm_window, (0, 0))
    b1 = draw_rect(20, 300, 135, 28)
    b2 = draw_rect(20, 350, 135, 28)
    b3 = draw_rect(20, 400, 135, 28)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(event.pos):
                clicked_sound()
                execfile("data/script.py")
                print("Button start pressed.")
            if b2.collidepoint(event.pos):
                clicked_sound()
                execfile("data/about.py")
                print("Button about pressed.")
                print("Nothing happened.")
            if b3.collidepoint(event.pos):
                clicked_sound()
                print("Button quit pressed.")
                quit()
                running = False
                
    screen.draw.blit(st, (20, 300))
    screen.draw.blit(at, (20, 350))
    screen.draw.blit(qt, (20, 400))
    # updates the frames of the game 
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
            
