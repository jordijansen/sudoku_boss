class Printer:
    def print_sudoku(self, sudoku, box_width):
        y = 0
        while y < len(sudoku):
            if y % box_width == 0:
                print '-------------------------------'
            row_result = ''
            i = 0
            while i < len(sudoku[y]):
                if i % box_width == 0:
                    row_result += '|'
                row_result += ' '
                row_result += str(sudoku[y][i])
                row_result += ' '
                i += 1
            row_result += '|'
            print row_result
            y += 1
        print '-------------------------------'
