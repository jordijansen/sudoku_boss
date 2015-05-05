class Sudoku:
    sudoku = [[]]
    box_width = 3

    def __init__(self, sudoku, box_width):
        self.sudoku = sudoku
        self.box_width = box_width

    def get_value(self, row, col):
        return self.sudoku[row][col]

    def set_value(self, row, col, value):
        self.sudoku[row][col] = value
