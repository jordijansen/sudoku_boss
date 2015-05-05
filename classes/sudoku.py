class Sudoku:
    sudoku = [[]]
    boxwidth = 3

    def __init__(self, sudoku, boxwidth):
        self.sudoku = sudoku
        self.boxwidth = boxwidth

    def get_value(self, row, col):
        return self.sudoku[row][col]

    def set_value(self, row, col, value):
        self.sudoku[row][col] = value
