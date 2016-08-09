import pygame
import pygame.locals
import tile_set
import tile_map
import os

TILE_WIDTH = 32   # Width of each tile in pixels
TILE_HEIGHT = 32  # Height of each tile in pixels

TEXT_HEIGHT = 64  # Height of the text area at the bottom in pixels

if __name__ == '__main__':
    # Load level 1 (the only level so far)
    level = tile_map.TileMap(os.path.join("graphics", "level1.map"))

    # Initialize pyGame and set the window title.
    pygame.init()
    pygame.display.set_caption('The Game')

    # The screen's width and height are set based on the width and height of the loaded level.
    screen = pygame.display.set_mode((TILE_WIDTH * level.width, TILE_HEIGHT * level.height + TEXT_HEIGHT))

    # Load the tile set.
    tiles = tile_set.TileSet(os.path.join("graphics", "tiles.png"), TILE_WIDTH, TILE_HEIGHT)

    # Start with a black background.
    screen.fill((0, 0, 0))

    # Draw each tile of the level.
    for x in range(level.width):
        for y in range(level.height):
            tile_index = level.get(x, y)
            tile = tiles.get_tile(tile_index)
            # Draw the tile at coordinates (x,y).
            screen.blit(tile, (x * TILE_WIDTH, y * TILE_HEIGHT))

    # Create a font that that is size 32.
    basic_font = pygame.font.SysFont("comicsansms", 32)

    # Render the text in white, with anti-aliasing (font smoothing) enabled.
    text = basic_font.render('Hello World!', True, (255, 255, 255))

    # Determine the dimensions(bounding rectangle) of the rendered text.
    text_rect = text.get_rect()
    # Set the center of the text to be in the middle (horizontally),
    # and below the tiles (vertically).
    text_rect.centerx = TILE_WIDTH * level.width / 2
    text_rect.centery = TILE_HEIGHT * level.height + (TEXT_HEIGHT / 2)
    # Draw the text on the screen.
    screen.blit(text, text_rect)

    # Show in the window what we have drawn so far.
    pygame.display.flip()

    # Wait until the QUIT event is raised.
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass

def list_fonts():
    """Currently unused function to list all the fonts installed on this computer."""
    for f in pygame.font.get_fonts():
        print f
