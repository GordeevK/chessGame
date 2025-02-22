from piece import Piece


class Board:
    def __init__(self):
        self.__board = [
            [Piece("bR"), 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            [Piece("bP"), Piece("bP"), Piece("bP"), Piece("bP"), Piece("bP"), Piece("bP"), Piece("bP"), Piece("bP")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
    def print_board(self) -> None:
        print("   A  B  C  D  E  F  G  H")
        for id_line in range(8):
            print(8 - id_line, "|", end="")
            for square in self.__board[id_line]:
                if not square:
                    print("  |", end="")
                else:
                    print(square, end="|")
            print("")
        print("   A  B  C  D  E  F  G  H")

    def move(self, move_from, move_to):
        y1, x1 = move_from
        y2, x2 = move_to
        if self.__board[y1][x1] != None:
            if self.__board[y1][x1].can_move():
                print("move to", y2, x2)
            else:
                print("cant move")
        else:
            print("no piece")



