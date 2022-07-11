# Visual Novel Template - Skeleton for a new PyGame Kinectic Novel
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (0, 255, 255)
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("dejavu-sans", 22)
active_fps = False
# Define our character here.
class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("data/character.png"),
            pygame.image.load("data/character_angry.png")
            ]
        self.image = self.images[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        
# Define our class object named "MainMenu".
class MainMenu(object):
    def __init__(self):
        self.start = font.render("Start Game", True, WHITE)
        if not active_fps:
            self.get_fps = font.render("Get FPS", True, WHITE)
        else:
            self.get_fps = font.render("Stop FPS", True, WHITE)            
        self.quit = font.render("Quit Game", True, WHITE)
        
    def draw(self, surface):
        self.border = pygame.draw.rect(surface, SKYBLUE, (20, 280, 135, 170), 0, 12) # This is a frame for the button list.
        self.button_one = pygame.draw.rect(surface, BLUE, (20, 300, 135, 28), 0, 12)
        self.button_two = pygame.draw.rect(surface, BLUE, (20, 350, 135, 28), 0, 12)
        self.button_thr = pygame.draw.rect(surface, BLUE, (20, 400, 135, 28), 0, 12)
        surface.blit(self.start, (20, 300))
        surface.blit(self.get_fps, (20, 350))
        surface.blit(self.quit, (20, 400))
            
# initialize pygame and create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Novel")
clock = pygame.time.Clock() # Requires for second button.
mainmenu = MainMenu()
def fps_counter():
    fpstxt = font.render("FPS: %d" % int(clock.get_fps()), True, WHITE)
    screen.blit(fpstxt, (0, 0))
    return fpstxt
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mainmenu.button_one.collidepoint(event.pos):
                exec(open("data\script.py").read())
            if mainmenu.button_two.collidepoint(event.pos):
                if not active_fps:
                    active_fps = True
                else:
                    active_fps = False
            if mainmenu.button_thr.collidepoint(event.pos):
                print("Exiting....")
                running = False
                print("Exited!")

    # Update
    pygame.display.update() # optional
    
    # Draw / render
    screen.fill((0, 128, 255))
    mainmenu.draw(screen)
    if active_fps:
        fps_counter() # Disable in game, only count in main menu
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
