class SudokuBox:
    box = []

    def __init__(self, values):
        self.box = values

    def validate_box(self, value):
        if value in self.box:
            return False
        return True
