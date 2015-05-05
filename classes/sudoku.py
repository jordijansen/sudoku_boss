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

    def validate_row(self, row, value):
        sudokurow = self.sudoku[row]
        for position in sudokurow:
            if position == value:
                return False
        return True

    def validate_col(self, col, value):
        for row in self.sudoku:
            if row[col] == value:
                return False
        return True

    def validate_box(self, row, col, value):
        return True

