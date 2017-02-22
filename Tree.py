class Tree:

    sudoku = None
    childs = []

    def __init__(self, a_sudoku):
        self.sudoku = a_sudoku

    def set_child(self, tree):
        self.childs.append(tree)
