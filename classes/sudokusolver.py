from copy import copy


class BruteForce:
    possiblevalues = []
    maxvalue = 0

    def solve(self, sudoku):
        self.maxvalue = sudoku.boxpercol * sudoku.boxperrow
        self.possiblevalues = range(1, self.maxvalue + 1)
        solvedsudoku = self.solve_step(sudoku, 0, 0)

        return solvedsudoku


    def solve_step(self, sudoku, row, col):
        currentsudoku = copy(sudoku)
        nextpositions = self.calculate_next_position(currentsudoku, row, col)

        if sudoku.get_value(row, col) == 0:
            for value in self.possiblevalues:
                if sudoku.validate_all(row, col, value):
                    currentsudoku.set_value(row, col, value)
                    print currentsudoku

                    if nextpositions is not None:
                        return self.solve_step(currentsudoku, nextpositions[0], nextpositions[1])
                    else:
                        print "done"
                        print currentsudoku
                        return currentsudoku
        else:
            return self.solve_step(currentsudoku, nextpositions[0], nextpositions[1])


    def calculate_next_position(self, sudoku, currentrow, currentcol):
        maxrow = len(sudoku.sudoku)
        maxcol = len(sudoku.sudoku[0])

        if currentcol < maxcol - 1:
            return [currentrow, currentcol + 1]
        else:
            if currentrow < maxrow - 1:
                return [currentrow + 1, 0]
            else:
                return None









