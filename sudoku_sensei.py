import sys
import Sudoku
import Tree


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print("You should pass the path to the sudoku file as an argument of the script.")
        exit()

    sudoku = Sudoku.Sudoku(sys.argv[1])
    Sudoku.resolve(Tree.Tree(sudoku))
