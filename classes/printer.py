class Printer:
    def printsudoku(self, sudoku, boxwidth):
        y = 0
        while y < len(sudoku):
            if y % boxwidth == 0:
                print '-------------------------------'
            rowresult = ''
            i = 0
            while i < len(sudoku[y]):
                if i % boxwidth == 0:
                    rowresult += '|'
                rowresult += ' '
                rowresult += str(sudoku[y][i])
                rowresult += ' '
                i += 1
            rowresult += '|'
            print rowresult
            y += 1
        print '-------------------------------'
