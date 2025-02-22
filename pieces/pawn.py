from piece import Piece


class Pawn(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "P"

    def can_move(self, move_from, move_to):
        x1, y1 = move_from
        x2, y2 = move_to
        y1, y2 = int(y1), int(y2)
        print(x1, x2, y1, y2)
        if x1 == x2:
            if self.is_white() and ((y2 - y1 == 1) or (y2 - y1 == 2 and self.is_first_move())):
                return True
            elif not self.is_white() and ((y2 - y1 == -1) or (y2 - y1 == -2 and self.is_first_move())):
                return True
        return False

    def can_capture(self, move_from, move_to):
        x1, y1 = move_from
        x2, y2 = move_to
        coordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        x1, x2, y1, y2 = int(coordinates.index(x1)), int(coordinates.index(x2)), int(y1), int(y2)
        print(x1, x2, y1, y2)
        if (x1 - x2 == 1) or (x1 - x2 == -1):
            if self.is_white() and (y2 - y1 == 1):
                return True
            elif not self.is_white() and (y2 - y1 == -1):
                return True



pawn = Pawn("White")
print(pawn.can_capture("D4", "E5"))
