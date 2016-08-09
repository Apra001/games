import pygame.image as pi

"""
A tile set is a single image with multiple tiles in it, organized into rows and columns. The TileSet class loads a tile
set into memory and supports addressing and retrieving tiles by index. For example, suppose that there is a tile set
image that is 40 x 20 pixels wide, with 10 x 10 tiles.

This means that 4 x 2 = 8 tiles can fit on this tile map:

  1234
  5678

Based on the following example, a tile set would loaded using:

  tile_set = tile_set.TileSet("tiles.png", 10, 10)

where "tiles.png" is the 40 x 20 pixel image, consisting of 10 x 10 tiles.
"""


class TileSet(object):
    """Represents a tile set."""

    def __init__(self, file_name, tile_width, tile_height):
        # Load the tile set image into memory using the PyGame library.
        tile_image = pi.load(file_name).convert()

        # Determine the size of the loaded image (in pixels).
        image_width, image_height = tile_image.get_size()

        # Calculate how many tiles wide and tall the tile set is.
        set_width = image_width / tile_width
        set_height = image_height / tile_height

        # Create a new list of individual tiles.
        self.tiles = []

        # Extract each tile, starting from the leftmost at the top, ending at the rightmost at the bottom.
        for y in range(set_height):
            for x in range(set_width):
                # Extract the tile at coordinates (x,y).
                rect = (x * tile_width, y * tile_height, tile_width, tile_height)
                self.tiles.append(tile_image.subsurface(rect))

        # The maximum index is width x height.
        self.max_index = set_width * set_height

    def get_tile(self, index):
        """Returns the tile at the given index."""
        if index >= self.max_index:
            raise ValueError("Tile set index %d must be less than %d." % (index, self.max_index))
        return self.tiles[index]
