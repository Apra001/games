import csv


class TileMap(object):
    """Represents a map in CSV format"""

    def __init__(self, map_file_name):
        self.rows = []
        self.width = 0
        self.height = 0
        with open(map_file_name, 'rb') as map_file:
            reader = csv.reader(map_file, delimiter=',')
            for line in reader:
                self.height += 1
                row = map(int, line)
                if self.width == 0:
                    self.width = len(row)
                else:
                    if len(row) != self.width:
                        raise "The number of values in row %d of %s is not %d." % (
                            self.height, map_file_name, self.width)
                self.rows.append(map(int, row))

        self.height = len(self.rows)

    def get(self, x, y):
        return self.rows[y][x]
