class SudokuBox:
    box = None
    numbersperrow = 0
    numberspercol = 0

    def __init__(self, numbersperrow, numberspercol):
        self.numbersperrow = numbersperrow
        self.numberspercol = numberspercol
        self.generate_box(numbersperrow, numberspercol)

    def generate_box(self, numbersperrow, numberspercol):
        self.box = [[0 for y in xrange(numberspercol)] for x in xrange(numbersperrow)]

    def get_box(self):
        return self.box

    def validate_box(self, value):
        if value in self.box:
            return False
        return True
