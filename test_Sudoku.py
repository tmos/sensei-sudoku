import Sudoku

def test_good_sudoku():
    s = Sudoku.Sudoku("sudoku_games_files/sudoku_easy_01")
    assert type(s) is Sudoku.Sudoku
    assert s.check_constraints() is True

def test_bad_sudoku():
    s = Sudoku.Sudoku("sudoku_games_files/sudoku_wrong")
    assert type(s) is Sudoku.Sudoku
    assert s.check_constraints() is False
