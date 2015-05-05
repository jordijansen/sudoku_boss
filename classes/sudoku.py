class Sudoku:
    sudoku = [[]]
    boxperrow = 3
    boxpercol = 3

    boxlist = []

    def __init__(self, sudoku, boxperrow, boxpercol):
        self.sudoku = sudoku
        self.boxperrow = boxperrow
        self.boxpercol = boxpercol
        self.fill_boxlist(boxperrow, boxpercol)

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
        box = self.get_box(row, col)
        maxxvalue = box[0] + self.boxperrow
        maxyvalue = box[1] + self.boxpercol

        for x in range(box[0], maxxvalue):
            for y in range(box[1], maxyvalue):
                if self.get_value(x, y) == value:
                    return False
        return True


    def get_box(self, row, col):
        for item in self.boxlist:
            if item[0] <= row < item[0] + self.boxperrow:
                if item[1] <= col < item[1] + self.boxpercol:
                    return item
        return [0, 0]

    def fill_boxlist(self, boxperrow, boxpercol):
        xvalue = 0
        maxvalue = boxperrow * boxpercol

        while xvalue < maxvalue:
            yvalue = 0
            while yvalue < maxvalue:
                self.boxlist.append([xvalue, yvalue])
                yvalue += boxpercol
            xvalue += boxperrow

    def validate_all(self, row, col, value):
        if self.validate_row(row, value):
            if self.validate_col(col, value):
                if self.validate_box(row, col, value):
                    return True
        return False








