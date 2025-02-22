class Piece:
    def __init__(self, color: str):
        self.color = color
        self.first_move = True
        self.can_capture = False

    def __str__(self):
        return self.color[0].lower()

    def can_move(self, move_from, move_to):
        return True

    def move(self):
        self.first_move = False

    def is_first_move(self):
        return self.first_move

    def is_white(self):
        if self.color == "White":
            return True
        return False

    def is_can_be_captured(self):
        return True


