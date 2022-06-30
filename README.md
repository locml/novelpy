# NovelPy 1.0

My visual novel I wrote for fun okay? You have chance to try it!
Made with Python 3.5 and Pygame SDL2


# Required to play it and build!

Python 3.5 to later: https://python.org

pygame_sdl2: https://github.com/renpy/pygame_sdl2 / https://test.pypi.org/project/pygame_sdl2

pygame (replacement) : pygame.org

py2exe: https://pypi.org/project/py2exe


This is the first scene from the script.py on the start_scene().

```python
def start_scene():

    # Here's the code of the scene, my bad coding :(
      
    running = True
    
    text = font.render("Hi this is cardcaptor sakura opening, want to try ?", True, white)
    
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
```    
