from piece import Piece


class Pawn(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "P"

    def can_move(self, move_from, move_to):
        x1, y1 = move_from
        x2, y2 = move_to
        if x1 == x2:
            if self.is_white() and ((int(y2) - int(y1) == 1) or (int(y2) - int(y1) == 2 and self.is_first_move())):
                return True
            elif not self.is_white() and ((int(y2) - int(y1) == -1) or (int(y2) - int(y1) == -2 and self.is_first_move())):
                return True

