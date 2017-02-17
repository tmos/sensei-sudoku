import Square

class Grid:
    """
    Main class for the mansion cleaning game.
    """
    instance = None
    sudoku = None
    constraints = None

    def __init__(self):
        """
        Grid constructor
        """
        if not self.instance:
            self.instance = self

        self.construct_constraints()

    def get_grid(self):
        if not self.instance:
            self.__init__()

    def set_sudoku(self, text):
        """
        Fill the grid with the text input sudoku
        :param text: text input
        :return: boolean, true if the filling as been made successfully
        """
        # TODO vérifier (algo qui transforme le texte en sudoku)
        matrix = None
        e = 0
        if len(text) > 81:
            return False
        for j in range(0, 9):
            for i in range(0, 9):
                if text[e] in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    matrix[j][i] = text[e]
                else:
                    matrix[j][i] = None
                e += 1
        self.sudoku = matrix
        return True

  #  def construct_constraints(self):
  #      """
  #      Fill the constraints list with all the grid constraints
  #      """
  #      constraints = []
  #      for j in range(0, 9):
  #          for i in range(0, 9):
  #              line = get_column_list(j)
  #              constraints += get_line_list(i)

    def print_sudoku(self):
        """
        Print the sudoku
        """
        print('+ - - - + - - - + - - - +')
        print('| ' + self.square_to_string(0, 0) + ' ' + self.square_to_string(0, 1) + ' ' + self.square_to_string(0, 2)
              + ' | ' + self.square_to_string(0, 3) + ' ' + self.square_to_string(0, 4) + ' ' + self.square_to_string(0, 5)
              + ' | ' + self.square_to_string(0, 6) + ' ' + self.square_to_string(0, 7) + ' ' + self.square_to_string(0, 8)
              + ' |')
        print('| ' + self.square_to_string(1, 0) + ' ' + self.square_to_string(1, 1) + ' ' + self.square_to_string(1, 2)
              + ' | ' + self.square_to_string(1, 3) + ' ' + self.square_to_string(1, 4) + ' ' + self.square_to_string(1, 5)
              + ' | ' + self.square_to_string(1, 6) + ' ' + self.square_to_string(1, 7) + ' ' + self.square_to_string(1, 8)
              + ' |')
        print('| ' + self.square_to_string(2, 0) + ' ' + self.square_to_string(2, 1) + ' ' + self.square_to_string(2, 2)
              + ' | ' + self.square_to_string(2, 3) + ' ' + self.square_to_string(2, 4) + ' ' + self.square_to_string(2, 5)
              + ' | ' + self.square_to_string(2, 6) + ' ' + self.square_to_string(2, 7) + ' ' + self.square_to_string(2, 8)
              + ' |')
        print('+ - - - + - - - + - - - +')
        print('| ' + self.square_to_string(3, 0) + ' ' + self.square_to_string(3, 1) + ' ' + self.square_to_string(3, 2)
              + ' | ' + self.square_to_string(3, 3) + ' ' + self.square_to_string(3, 4) + ' ' + self.square_to_string(3, 5)
              + ' | ' + self.square_to_string(3, 6) + ' ' + self.square_to_string(3, 7) + ' ' + self.square_to_string(3, 8)
              + ' |')
        print('| ' + self.square_to_string(4, 0) + ' ' + self.square_to_string(4, 1) + ' ' + self.square_to_string(4, 2)
              + ' | ' + self.square_to_string(4, 3) + ' ' + self.square_to_string(4, 4) + ' ' + self.square_to_string(4, 5)
              + ' | ' + self.square_to_string(4, 6) + ' ' + self.square_to_string(4, 7) + ' ' + self.square_to_string(4, 8)
              + ' |')
        print('| ' + self.square_to_string(5, 0) + ' ' + self.square_to_string(5, 1) + ' ' + self.square_to_string(5, 2)
              + ' | ' + self.square_to_string(5, 3) + ' ' + self.square_to_string(5, 4) + ' ' + self.square_to_string(5, 5)
              + ' | ' + self.square_to_string(5, 6) + ' ' + self.square_to_string(5, 7) + ' ' + self.square_to_string(5, 8)
              + ' |')
        print('+ - - - + - - - + - - - +')
        print('| ' + self.square_to_string(6, 0) + ' ' + self.square_to_string(6, 1) + ' ' + self.square_to_string(6, 2)
              + ' | ' + self.square_to_string(6, 3) + ' ' + self.square_to_string(6, 4) + ' ' + self.square_to_string(6, 5)
              + ' | ' + self.square_to_string(6, 6) + ' ' + self.square_to_string(6, 7) + ' ' + self.square_to_string(6, 8)
              + ' |')
        print('| ' + self.square_to_string(7, 0) + ' ' + self.square_to_string(7, 1) + ' ' + self.square_to_string(7, 2)
              + ' | ' + self.square_to_string(7, 3) + ' ' + self.square_to_string(7, 4) + ' ' + self.square_to_string(7, 5)
              + ' | ' + self.square_to_string(7, 6) + ' ' + self.square_to_string(7, 7) + ' ' + self.square_to_string(7, 8)
              + ' |')
        print('| ' + self.square_to_string(8, 0) + ' ' + self.square_to_string(8, 1) + ' ' + self.square_to_string(8, 2)
              + ' | ' + self.square_to_string(8, 3) + ' ' + self.square_to_string(8, 4) + ' ' + self.square_to_string(8, 5)
              + ' | ' + self.square_to_string(8, 6) + ' ' + self.square_to_string(8, 7) + ' ' + self.square_to_string(8, 8)
              + ' |')
        print('+ - - - + - - - + - - - +')

    def square_to_string(self, j, i):
        """
        Converts a square to string
        :param j: the y position into the grid
        :param i: the x position into the grid
        :return: the string value of the square
        """
        case = self.sudoku[j][i]
        if case:  # There is a value into the case
            return case
        else:
            return '.'
