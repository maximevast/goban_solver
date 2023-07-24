import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """
    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban
        self.checked = []

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if not self.goban or x < 0 or y < 0 or y >= len(self.goban) or x >= len(self.goban[0]):
            return Status.OUT
        elif self.goban[y][x] == '.':
            return Status.EMPTY
        elif self.goban[y][x] == 'o':
            return Status.WHITE
        elif self.goban[y][x] == '#':
            return Status.BLACK

    def is_taken(self, x, y, checked=None):
        """
        Recursively find out if a given position in taken
        
        Args:
            x: the x coordinate (integer)
            y: the y coordinate (integer)
            checked: an array of already verified coordinates (tupples of integers)

        Returns:
            a Boolean
        """
        color = self.get_status(x, y)
        surroundings = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
        # Initialize mutable checked
        if checked is None:
            checked = []
       
        for coords in list(set(surroundings) - set(checked)):
            checked.append(coords)
            status = self.get_status(*coords)
            if status == Status.EMPTY or (status == color and not self.is_taken(*coords, checked=checked)):
                return False

        return True
