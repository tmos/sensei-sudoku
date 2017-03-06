import sys
import Sudoku
import Tree

#sys.setrecursionlimit(999999999)  # Disable stack size limit

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print("You should pass the path to the sudoku file as an argument of the script.")
        exit()

    s = Sudoku.Sudoku(sys.argv[1])
    Sudoku.resolve(s)
