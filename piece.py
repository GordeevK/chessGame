class Piece:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def can_move(self):
        return True


piece = Piece("bR")
print(piece)