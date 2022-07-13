# PyGame Novel
A visual novel I wrote for fun okay? You have chance to try it!.

It's still in development, so something here not so good and can contains a lot of errors..


# New update

## Building

Change how game2exe.py works when building the game, allowed to rebuild the game on released version, rename game2exe.py to build_win.py, added a console version of the build_exe.py for rebuild the game.

Return build_zip.py with some new code there.

## Scripting
Instead of draw text and text area, now just had to write this in the outside loop.
```py
textbox = Textbox(surface, color, x, y, width, height, border) # Replace surface, color, x, y, width, height, border with your code.
all_sprites.add(textbox) # textbox is a sprite object and all_sprites is a group object.
# Write this in the in game loop
all_sprites.draw(surface, text, x, y)# Replace surface, text, x, y with your code.
```

# Bonus
Now the text is rendered letter by letter, just need to change ```self.count += 0.5``` with your number so the will rendering letter with the time you just set in ```self.count```

# Final
I'm had removed the Download Page by now, if you want to download the project use source code and releases page instead.



