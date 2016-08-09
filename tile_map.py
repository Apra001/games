import csv

"""
This module is responsible for loading the map of a level. Maps are stored in CSV (comma-separated values) files. Each
number in the file is an index to a tile in the tile set.

For example, suppose that there is a tile set where index 0 represents a tile of grass, 1 represents a tile of road and
2 represents a tile of water. A tile map file containing the following:

0,0,1,0,0
0,0,1,0,0
0,0,1,0,0
2,2,2,2,2
2,2,2,2,2

will be shown as a 5 by 5 level. The level has a field of grass, with a vertical road running from the top to water at
the bottom.

To use the class, create a new instance with the filename passed in as an argument:

  level = tile_map.TileMap("level.map"))

where "level.map" is an example of a filename. Then, tiles can be accessed using the get() method by x and y
coordinates. For example, level.get(0,0) returns 0, level.get(2,0) returns 1, level.get(0,3) returns 2 (coordinates are
0-based).

The dimensions of the map are detected automatically, based on the number of values in the first row and the number of
rows. If the length of the rows is inconsistent, then an exception is thrown. For example, you cannot have one row with
5 tiles and another with 6.
"""


class TileMap(object):
    """Represents the map of a level in CSV format"""

    def __init__(self, map_file_name):
        self.rows = []
        self.width = 0
        self.height = 0
        with open(map_file_name, 'rb') as map_file:
            reader = csv.reader(map_file, delimiter=',')
            for line in reader:
                # Height is incremented for each new line.
                self.height += 1
                # Call the int() function on each element of the string values read.
                row = map(int, line)
                if self.width == 0:
                    # After reading the first row, the width is set, then it cannot change.
                    self.width = len(row)
                else:
                    if len(row) != self.width:
                        # All rows must be the same length as the first one.
                        raise "The number of values in row %d of %s is not %d." % (
                            self.height, map_file_name, self.width)
                # Each row contains an array of index values.
                self.rows.append(row)
        # The height is determined by the total number of lines read.
        self.height = len(self.rows)

    def get(self, x, y):
        """Returns the index of a tile for the given (x,y) coordinates."""
        return self.rows[y][x]
