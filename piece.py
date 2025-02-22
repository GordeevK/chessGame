class Piece:
    def __init__(self, name: str, color: str):
        self.__name = name
        self.__color = color

    def __str__(self):
        return self.__color[0].lower() + self.__name[0].upper()

    def can_move(self, move_from, move_to):
        y1, x1 = move_from
        y2, x2 = move_to
        return True
    def can_capture(self,move_from, move_to):
        return True


piece = Piece("Pawn", "Black")
print(piece)