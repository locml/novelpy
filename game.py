# -*- encoding: utf-8 -*-
import pygame, sys

WIDTH = 1184 # Resizable window width
HEIGHT = 666 # Resizable window height
FPS = 240

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (0, 255, 255)
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("dejavu-sans", 25)
active_fps = False
# Define our character here.
class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("data/placeholder.png").convert(),
            pygame.image.load("data/placeholder_end.png").convert()
            ]
        self.image = self.images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center
        
# Define our class object named "MainMenu".
class MainMenu(object):
    def __init__(self):
        self.start = font.render("Start Game", True, WHITE)
        self.get_fps = font.render("Get FPS", True, WHITE)           
        self.quit = font.render("Quit Game", True, WHITE)
        
    def draw(self, surface):
        self.border = pygame.draw.rect(surface, SKYBLUE, (20, 280, 200, 170), 0, 12) # This is a frame for the button list.
        self.button_one = pygame.draw.rect(surface, BLUE, (20, 300, 200, 28), 0, 12)
        self.button_two = pygame.draw.rect(surface, BLUE, (20, 350, 200, 28), 0, 12)
        self.button_thr = pygame.draw.rect(surface, BLUE, (20, 400, 200, 28), 0, 12)
        surface.blit(self.start, (25, 300))
        surface.blit(self.get_fps, (25, 350))
        surface.blit(self.quit, (25, 400))
class Textbox(pygame.sprite.Sprite):
    
    def __init__(self, surface, color, x, y, width, height, border):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.set_alpha(200)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.textbox_area = (self.rect.x, self.rect.y, width, height)
        pygame.draw.rect(surface, color, self.textbox_area, 0, border)
        self.count = 0
    def draw(self, surface, text, x, y):
        self.count += 0.5
        self.dialog = font.render(text[:int(self.count)], True, WHITE)
        surface.blit(self.dialog, (x, y))
        return self.count
# initialize pygame and create window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Template")
clock = pygame.time.Clock() # Requires for second button.
mainmenu = MainMenu()

def fps_counter():
    fps_count = int(clock.get_fps())
    fpstxt = font.render("FPS: %d" % fps_count, True, WHITE)
    screen.blit(fpstxt, (0, 0))
    return fps_count

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
                running = False

    # Update
    pygame.display.update() # optional
    
    # Draw / render
    screen.fill((0, 128, 255))
    mainmenu.draw(screen)
    if active_fps:
        fps_counter()
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
