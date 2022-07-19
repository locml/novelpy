test = False # Did you has ended the test ?
def start_scene():
    pg.init()
    all_sprites = pg.sprite.Group()
    char = Character()
    textbox = Textbox(g.screen, (50, 50, 50), 0, 430, 1280, 300, 12)
    all_sprites.add(char)
    all_sprites.add(textbox)
    running = True
    while running:
        g.clock.tick(FPS)
        g.dt = int(g.clock.get_fps())
        g.screen.fill((0, 128, 255))
        all_sprites.draw(g.screen)
        textbox.draw(g.screen, "Hi this is a test dialogue, please continue by using mouse.", 20, 430)
        if g.active_fps:
            g.fps_counter()
        pg.display.update()
        all_sprites.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return
    
def second_scene():
    pg.init()
    all_sprites = pg.sprite.Group()
    char = Character()
    textbox = Textbox(g.screen, (50, 50, 50), 0, 430, 1280, 300, 12)
    all_sprites.add(char)
    all_sprites.add(textbox)
    running = True
    narrator = font.render("Place", True, GREEN)
    while running:
        g.clock.tick(FPS)
        g.dt = int(g.clock.get_fps())
        g.screen.fill((0, 128, 255))
        all_sprites.draw(g.screen)
        textbox.draw(g.screen, "This is another dialogue for this example with my name here!", 20, 460)
        g.screen.blit(narrator, (20, 430))
        if g.active_fps:
            g.fps_counter()
        pg.display.update()
        all_sprites.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return
            
            
def end_scene():
    pg.init()
    running = True
    test = True
    all_sprites = pg.sprite.Group()
    char = Character()
    char.image = char.images[1].convert_alpha()
    char.image.set_colorkey(WHITE)   
    textbox = Textbox(g.screen, (50, 50, 50, 150), 0, 430, 1280, 300, 12 )
    all_sprites.add(char)
    all_sprites.add(textbox)
    while running:
        g.clock.tick(FPS)
        g.dt = int(g.clock.get_fps())
        g.screen.fill((0, 128, 255))
        all_sprites.draw(g.screen)
        textbox.draw(g.screen, "I hope you will did a best game! So boring when you had to go...", 20, 430)
        if g.active_fps:
            g.fps_counter()
        pg.display.update()
        all_sprites.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                char.kill()
                textbox.kill()
                return

if __name__ == "__main__":
    start_scene()
    second_scene()
    end_scene()
