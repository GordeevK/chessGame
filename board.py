class Board:
    def __init__(self):
        self.__board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
    def print_board(self) -> None:
        print("   1  2  3  4  5  6  7  8")
        for id_line in range(8):
            print((8 - id_line), "|", end="")
            for square in self.__board[id_line]:
                if not square:
                    print("  |", end="")
                else:
                    print(square + "|", end="")
            print("")
        print("   1  2  3  4  5  6  7  8")

a = Board()
a.print_board()
