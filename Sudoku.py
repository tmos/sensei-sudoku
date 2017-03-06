import Tree


class Sudoku:

    __sudoku = []

    def __init__(self, source):

        if type(source) is list:
            self.__sudoku = source

            if self.is_valid() is not True:
                exit("Sudoku is not valid")
        else:
            self.__sudoku = []
            file = open(source, "r")
            if file:
                for a_line in file.readlines():
                    tmp = []

                    for a_char in a_line:
                        if a_char != "\n":
                                tmp.append(int(a_char))

                    self.__sudoku.append(tmp)
            else:
                exit("File doesn't exists")

    def print_sudoku(self):
        print('\n')

        line_count = 0
        for a_line in self.__sudoku:

            tmp = ""
            case_count = 0
            for a_case in a_line:

                tmp += '   ' + str(a_case)
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

    def is_valid(self):
        """
        Fill the constraints list with all the grid constraints
        """

        def __lines_are_correct(su):
            is_ok = True

            for a_line in su:
                tmp = []

                for a_char in a_line:
                    if a_char is not 0:
                        if is_ok is True and a_char not in tmp:
                            tmp.append(a_char)
                        else:
                            is_ok = False

            return is_ok

        def __columns_are_correct(su):
            is_ok = True

            for x in range(len(su[0])):
                tmp = []

                for y in range(len(su)):
                    a_char = su[y][x]

                    if a_char is not 0:
                        if is_ok is True and a_char not in tmp:
                            tmp.append(a_char)
                        else:
                            is_ok = False

            return is_ok

        def __cases_are_correct(su):

            def check_a_case(start_x, start_y):
                case_is_ok = True
                tmp = []

                for x in range(start_x, start_x + 3):
                    for y in range(start_y, start_y + 3):
                        a_char = su[y][x]

                        if a_char is not 0:
                            if case_is_ok is True and a_char not in tmp:
                                tmp.append(a_char)
                            else:
                                return False

                return case_is_ok

            all_cases_are_ok = True

            if not check_a_case(0, 0) or not check_a_case(0, 3) or not check_a_case(0, 6) or \
                    not check_a_case(3, 0) or not check_a_case(3, 3) or not check_a_case(3, 6) or \
                    not check_a_case(6, 0) or not check_a_case(6, 3) or not check_a_case(6, 6):
                all_cases_are_ok = False

            return all_cases_are_ok

        if __lines_are_correct(self.__sudoku) and\
            __columns_are_correct(self.__sudoku) and\
                __cases_are_correct(self.__sudoku):
            return True
        else:
            return False

    def get_forbidden_values_for(self, y, x):
        forbidden_values = []

        if self.__sudoku[y][x] > 0:
            return [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # check column
        for iter_y in range(len(self.__sudoku[y])):
                a_char = self.__sudoku[iter_y][x]
                if a_char is not 0 and a_char not in forbidden_values:
                    forbidden_values.append(a_char)

        # check line
        for iter_x in range(len(self.__sudoku[x])):
            a_char = self.__sudoku[y][iter_x]
            if a_char is not 0 and a_char not in forbidden_values:
                forbidden_values.append(a_char)

        # check case
        start_x = 0
        start_y = 0
        # Compute in which square the value is
        if x < 3:
            start_x = 0
        elif x < 6:
            start_x = 3
        elif x < 9:
            start_x = 6

        if y < 3:
            start_y = 0
        elif y < 6:
            start_y = 3
        elif y < 9:
            start_y = 6

        for x in range(start_x, start_x + 3):
            for y in range(start_y, start_y + 3):
                a_char = self.__sudoku[y][x]

                if a_char is not 0 and a_char not in forbidden_values:
                    forbidden_values.append(a_char)

        return forbidden_values

    def get_remaining_values(self):
        # We take the cell with the biggest amount of forbidden values
        selected_cell = {'y': -1, 'x': -1, 'score': -1}

        for y in range(len(self.__sudoku)):
            for x in range(len(self.__sudoku[0])):
                if self.__sudoku[y][x] == 0:
                    how_many_constraints = len(self.get_forbidden_values_for(y, x))
                    if how_many_constraints > selected_cell['score']:
                        selected_cell = {'y': y, 'x': x, 'score': how_many_constraints}

        return selected_cell

    def get_possibilities_for(self, y, x):
        forbidden = self.get_forbidden_values_for(y, x)
        base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tmp = []
        for val in base:
            if val not in forbidden:
                tmp.append(val)

        return tmp

    def set(self, y, x, val):
        if self.__sudoku[y][x] > 0:
            print("NOPE : " + str(self.__sudoku[y][x]))

        self.__sudoku[y][x] = val
        return self.__sudoku

    def hash(self):
        res = ""
        for line in self.__sudoku:
            for char in line:
                res += str(char)

        return res

    def is_resolved(self):
        if self.is_valid():
            for line in self.__sudoku:
                for val in line:
                    if val is 0:
                        return False
            return True
        else:
            return False

log = []


def resolve(sudoku):
    sudoku.print_sudoku()

    if sudoku.is_resolved():
        print("finito !")
        return sudoku
    else:
        current_play = sudoku.get_remaining_values()

        x = current_play['x']
        y = current_play['y']

        what_to_play = sudoku.get_possibilities_for(y, x)

        if len(what_to_play):
            for move in what_to_play:
                new_sudoku = Sudoku(sudoku.get_sudoku())
                new_sudoku.set(y, x, move)

                log.append({'sudoku': new_sudoku.get_sudoku(), 'x': x, 'y': y, 'new_val': move})

                res = resolve(Sudoku(sudoku.get_sudoku()))
                if res is not None:
                    print("yeah")
        else:
            log.append("FAIL")
            return None
