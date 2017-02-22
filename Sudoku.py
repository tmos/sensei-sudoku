from collections import OrderedDict

class Sudoku :

    __sudoku = []

    def __init__(self, filename):
        file = open(filename, "r")
        if file:
            for a_line in file.readlines():
                tmp = []

                for a_char in a_line:
                    if a_char != "\n":
                        tmp.append(a_char)

                self.__sudoku.append(tmp)

    def print_sudoku(self):
        print('\n')

        line_count = 0
        for a_line in self.__sudoku:

            tmp = ""
            case_count = 0
            for a_case in a_line:

                tmp += '   ' + a_case
                if case_count == 2 or case_count == 5:
                    tmp += '    '

                case_count += 1

            print(tmp)

            if line_count == 2 or line_count == 5:
                print("\n")

            line_count += 1

        print('\n')

    def get_sudoku(self):
        return self.__sudoku

    def calculate(self):
        """
        Calculation to solve the sudoku problem
        """
        # TODO ajouter backtracking_search, ac-3 et tout le reste pour effectuer le calcul

    def check_constraints(self):
        """
        Fill the constraints list with all the grid constraints
        """
        print("lines : " + str(self.__lines_are_correct()))
        print("colum : " + str(self.__columns_are_correct()))
        print("cases : " + str(self.__cases_are_correct()))

    def __lines_are_correct(self):
        is_ok = True

        for a_line in self.__sudoku:
            tmp = []

            for a_char in a_line:
                if a_char is not ".":
                    if is_ok is True and a_char not in tmp:
                        tmp.append(a_char)
                    else:
                        is_ok = False

        return is_ok

    def __columns_are_correct(self):
        is_ok = True

        sudoku = self.__sudoku

        for x in range(len(sudoku[0])):
            tmp = []

            for y in range(len(sudoku)):
                a_char = sudoku[y][x]

                if a_char is not ".":
                    if is_ok is True and a_char not in tmp:
                        tmp.append(a_char)
                    else:
                        is_ok = False

        return is_ok

    def __cases_are_correct(self):
        is_ok = True
        return is_ok
