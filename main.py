from classes.printer import Printer
from classes.sudoku import Sudoku

puzzle = [
    [1, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

boxwidth = 3
boxheight = 3

boxvalues = []

for row in puzzle:
    offset = 0
    counter = 0

    splitted = row[offset:len(row)/boxwidth]
    print splitted


printer = Printer()
sudoku = Sudoku(puzzle, 3)

printer.print_sudoku(sudoku.sudoku, sudoku.box_width)
