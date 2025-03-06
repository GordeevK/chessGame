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

    def can_capture(self, move_from: str, move_to: str) -> bool:
        x1_str, y1 = move_from[0], int(move_from[1])
        x2_str, y2 = move_to[0], int(move_to[1])

        x1 = ord(x1_str.upper()) - ord('A') + 1
        x2 = ord(x2_str.upper()) - ord('A') + 1

        if abs(x1 - x2) == 1:
            if (y1 - y2 == -1 and self.is_white()) or (y1 - y2 == -1 and not self.is_white()):
                return True
        return False


pawn = Pawn("White")
print(pawn.can_capture("D4", "C5"))


