from piece import Piece


class Bishop(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "B"

    def can_move(self, move_from, move_to, board: list[list]) -> bool:
        if not (0 <= move_to[0] < 8 and 0 <= move_to[1] < 8):
            return False
        target_piece = board[move_to[0]][move_to[1]]
        if target_piece is not None and target_piece.is_white() == self.is_white():
            return False
        if not self.is_clear_path(move_from, move_to, board):
            return False
        return True

    def get_possible_moves(self, board: list[list]) -> list[tuple]:
        moves = []
        move_from = self.get_pos()
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            x, y = move_from
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:  # Пока не выйдем за пределы доски
                x += dx
                y += dy
                if self.can_move(move_from, (x, y), board):
                    moves.append((x, y))
                if board[x][y] is not None:
                    break
        return moves


# Пример использования
board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, Piece(color="Black", position=(6, 6)), None],
    [None, None, None, None, None, None, None, None]
]

# Пример: создание фигуры (слона)
bishop = Bishop(color="White", position=(4, 4))

# Получение всех возможных ходов для слона
possible_moves = bishop.get_possible_moves(board)
print(possible_moves)
