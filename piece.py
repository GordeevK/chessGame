class Piece:
    def __init__(self, color: str):
        self.color = color
        self.first_move = True

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

