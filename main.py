import pygame as pg
from pygame.locals import *
import sys

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKYBLUE = (0, 255, 255)
BLUE = (0, 0, 255)
# game settings
WIDTH = 1184
HEIGHT = 666
new_fps = 0
new_count = 0
TITLE = "Template"
BGCOLOR = (112, 146, 190)
pg.font.init()
font = pg.font.SysFont("dejavu-sans", 25)
# Define our character here.
class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = [
            pg.image.load("data/placeholder.png").convert(),
            pg.image.load("data/placeholder_end.png").convert()
            ]
        self.image = self.images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = g.screen.get_rect().center
        
if new_fps > 0:
    FPS = new_fps
else:
    FPS = 240
    
class Textbox(pg.sprite.Sprite):
    
    def __init__(self, surface, color, x, y, width, height, border):
        pg.sprite.Sprite.__init__(self)
        self.textbox_area = (x, y, width, height)
        self.rect = self.textbox_area
        pg.draw.rect(surface, color, self.textbox_area, 0, 12)
        self.image = pg.Surface((width, height))
        self.image.set_alpha(200)
        self.count = 0
    def draw(self, surface, text, x, y):
        if new_count != 0:
            self.count += new_count
        else:
            self.count += 0.5
        self.dialog = font.render(text[:int(self.count)], True, WHITE)
        surface.blit(self.dialog, (x, y))
        return self.count
    
# Define our loop named "Game".
        
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def fps_counter(self):
        self.fpstxt = font.render("FPS: %d" % self.dt, True, WHITE)
        self.screen.blit(self.fpstxt, (0, 0))
        return self.dt
    
    def load_data(self):
        self.active_fps = False
        
    def main_menu(self):
        self.start = font.render("Start Game", True, WHITE)
        self.get_fps = font.render("Get FPS", True, WHITE)           
        self.quit = font.render("Quit Game", True, WHITE)
        self.border = pg.draw.rect(self.screen, SKYBLUE, (20, 280, 200, 170), 0, 12) # This is a frame for the button list.
        self.button_one = pg.draw.rect(self.screen, BLUE, (20, 300, 200, 28), 0, 12)
        self.button_two = pg.draw.rect(self.screen, BLUE, (20, 350, 200, 28), 0, 12)
        self.button_thr = pg.draw.rect(self.screen, BLUE, (20, 400, 200, 28), 0, 12)
        self.screen.blit(self.start, (25, 300))
        self.screen.blit(self.get_fps, (25, 350))
        self.screen.blit(self.quit, (25, 400))
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = int(self.clock.tick(FPS))
            self.events()
            self.update()
            self.draw()

    def update(self):
        # update position of the game loop
        pass

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.main_menu()
        if self.active_fps:
            self.fps_counter()
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == QUIT:
                self.playing = False
                pg.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN :
                if self.button_one.collidepoint(event.pos):
                    exec(open('data\script.py').read())
                if self.button_two.collidepoint(event.pos):
                    if self.active_fps == False:
                        self.active_fps = True
                    else:
                        self.active_fps = False
                if self.button_thr.collidepoint(event.pos):
                    self.playing = False
                    pg.quit()
                    sys.exit()

# create the game object
g = Game()
while True:
    g.run()
