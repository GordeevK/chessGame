from typing import Tuple

from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.knight import Knight


class Board:
    def __init__(self):
        self.__board = [
            [Rook("Black", (0, 0)), Knight("Black", (0, 1)), Bishop("Black", (0, 2)), Queen("Black", (0, 3)),
             King("Black", (0, 4)), Bishop("Black", (0, 5)), Knight("Black", (0, 6)), Rook("Black", (0, 7))],
            [Pawn("Black", (1, 0)), Pawn("Black", (1, 1)), Pawn("Black", (1, 2)), Pawn("Black", (1, 3)),
             Pawn("Black", (1, 4)), Pawn("Black", (1, 5)), Pawn("Black", (1, 6)), Pawn("Black", (1, 7))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("White", (6, 0)), Pawn("White", (6, 1)), Pawn("White", (6, 2)), Pawn("White", (6, 3)),
             Pawn("White", (6, 4)), Pawn("White", (6, 5)), Pawn("White", (6, 6)), Pawn("White", (6, 7))],
            [Rook("White", (7, 0)), Knight("White", (7, 1)), Bishop("White", (7, 2)), Queen("White", (7, 3)),
             King("White", (7, 4)), Bishop("White", (7, 5)), Knight("White", (7, 6)), Rook("White", (7, 7))],
        ]
        self.__coordinates = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['8', '7', '6', '5', '4', '3', '2', '1']
        ]

    def print_board(self):
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

    def print_piece_position(self, move_from):
        x1, y1 = self.split_coordinates(move_from)
        piece = self.__board[y1][x1]
        print(piece)

    def print_piece_possible_moves(self, move_from):
        x1, y1 = self.split_coordinates(move_from)
        piece = self.__board[y1][x1].get_possible_moves(self.__board)
        print(piece)
        print(y1, x1)

    def move(self, move_from: str, move_to: str) -> None:
        x1, y1 = self.split_coordinates(move_from)
        x2, y2 = self.split_coordinates(move_to)
        piece = self.__board[y1][x1]
        if (y2, x2) in piece.get_possible_moves(self.__board):
            piece.move()
            self.__board[y2][x2] = piece
            self.__board[y1][x1] = None
        else:
            print("Невозможный ход для фигуры")

    def split_coordinates(self, coordinates: str) -> tuple[int, int]:
        letter = coordinates[0]
        number = coordinates[1]
        return self.get_position((letter, number))

    def get_position(self, position: tuple[str, str]) -> tuple[int, int]:
        x = self.__coordinates[0].index(position[0])
        y = self.__coordinates[1].index(position[1])
        return x, y


