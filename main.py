from classes.printer import Printer
from classes.sudoku import Sudoku

printer = Printer()
sudoku = Sudoku()

printer.printsudoku(sudoku.sudoku, sudoku.boxwidth)