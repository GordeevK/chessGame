from piece import Piece


class Pawn(Piece):
    def __init__(self, color: str):
        self.__color = color
        self.can_move_through = False
        self.first_move
    def __str__(self) -> str:
        return self.__color[0].lower() + "P"
    def can_move(self, move_from, move_to):
        y1, x1 = move_from
        y2, x2 = move_to
        if int(x1):
            return True