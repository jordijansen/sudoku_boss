from classes.printer import Printer
from classes.sudoku import Sudoku
from classes.sudokusolver import BruteForce

puzzle1 = [
    [0, 1, 0, 0],
    [0, 0, 3, 0],
    [0, 0, 4, 0],
    [2, 0, 0, 0]
]

puzzle2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

puzzle3 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

puzzle4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

printer = Printer()

sudoku_puzzle1 = Sudoku(puzzle1, 2, 2)
sudoku_puzzle2 = Sudoku(puzzle2, 3, 3)
sudoku_puzzle3 = Sudoku(puzzle3, 3, 3)
sudoku_puzzle4 = Sudoku(puzzle4, 2, 2)

forcer = BruteForce()

solvedsudoku = None

print '------------- The Sudoku Solver Brute Kracht -------------'
print 'First choose the sudoku you want to solve:'
print '1) 2x2 Sudoku - prefilled (16 positions)'
print '2) 3x3 Sudoku - empty (81 positions)'
print '3) 3x3 Sudoku - prefilled (81 positions)'
print '4) 2x2 Sudoku - empty (16 positions)'
var = int(raw_input("Please choose: "))
print 'You chose: ' + str(var)
print 'Solving the following puzzle: '
if var == 1:
    printer.print_sudoku(sudoku_puzzle1, 2)
    solvedsudoku = forcer.solve(sudoku_puzzle1)
    print 'Solved!!!!'
    printer.print_sudoku(solvedsudoku, 2)
if var == 2:
    printer.print_sudoku(sudoku_puzzle2, 3)
    solvedsudoku = forcer.solve(sudoku_puzzle2)
    print 'Solved!!!!'
    printer.print_sudoku(solvedsudoku, 3)
if var == 3:
    printer.print_sudoku(sudoku_puzzle3, 3)
    solvedsudoku = forcer.solve(sudoku_puzzle3)
    print 'Solved!!!!'
    printer.print_sudoku(solvedsudoku, 3)
if var == 4:
    printer.print_sudoku(sudoku_puzzle4, 2)
    solvedsudoku = forcer.solve(sudoku_puzzle4)
    print 'Solved!!!!'
    printer.print_sudoku(solvedsudoku, 2)

