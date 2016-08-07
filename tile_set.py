import pygame.image as pi


class TileSet(object):
    """Represents a tile set."""

    def __init__(self, filename, tile_width, tile_height):
        self.filename = filename
        self.tile_width = tile_width
        self.tile_height = tile_height
        tile_image = pi.load(filename).convert()
        image_width, image_height = tile_image.get_size()
        self.max_x = image_width / tile_width
        self.max_y = image_height / tile_height
        self.tiles = []
        for i in range(self.max_x * self.max_y):
            rect = ((i % self.max_x) * tile_width, i / self.max_x, tile_width, tile_height)
            self.tiles.append(tile_image.subsurface(rect))

    def get_tile(self, index):
        return self.tiles[index]
