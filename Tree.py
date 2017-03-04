class Tree:

    sudoku = None
    parent = None

    def __init__(self, a_sudoku, parent):
        self.sudoku = a_sudoku
        self.parent = parent

    def get_sudoku(self):
        return self.sudoku

    def get_parent(self):
        return self.parent
