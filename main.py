import pygame
import pygame.locals
import tile_set
import tile_map
import os

TILE_WIDTH = 32
TILE_HEIGHT = 32

TEXT_HEIGHT = 64

if __name__ == '__main__':

    level = tile_map.TileMap(os.path.join("graphics", "level1.map"))

    pygame.init()
    pygame.display.set_caption('The Game')

    screen = pygame.display.set_mode((TILE_WIDTH * level.width, TILE_HEIGHT * level.height + TEXT_HEIGHT))
    tiles = tile_set.TileSet(os.path.join("graphics", "tiles.png"), TILE_WIDTH, TILE_HEIGHT)
    screen.fill((0, 0, 0))

    for x in range(level.width):
        for y in range(level.height):
            tile_index = level.get(x, y)
            tile = tiles.get_tile(tile_index)
            screen.blit(tile, (x * TILE_WIDTH, y * TILE_HEIGHT))

    basicfont = pygame.font.SysFont("comicsansms", 32)
    text = basicfont.render('Hello World!', True, (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = TILE_WIDTH * level.width / 2
    textrect.centery = TILE_HEIGHT * level.height + (TEXT_HEIGHT / 2)
    screen.blit(text, textrect)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass


def list_fonts():
    for f in pygame.font.get_fonts():
        print f
