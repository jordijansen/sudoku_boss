from classes.sudokubox import SudokuBox

class Playfield:
    boxes = [[]]
    boxperrow = 0
    boxpercol = 0

    def __init__(self, boxperrow, boxpercol):
        self.boxperrow = boxperrow
        self.boxpercol = boxpercol
        self.generate_boxes(boxperrow, boxpercol)

    def generate_boxes(self, boxperrow, boxpercol):
        self.boxes = [[SudokuBox(boxperrow, boxpercol).get_box() for x in xrange(boxpercol)] for y in xrange(boxperrow)]

    def print_playfield(self):
        print self.boxes
