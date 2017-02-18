class Square:
    """
    This class is used to keep information about each square in each algorithm step possibility
    """
    x = None
    y = None
    domaines = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    contraintes = []

    def __init__(self, x, y):
        """
        Square constructor
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
