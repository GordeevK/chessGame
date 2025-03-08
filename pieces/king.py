from piece import Piece
from pieces.rook import Rook


class King(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "K"

    def get_possible_moves(self, board: list[list]) -> list[tuple]:
        moves = []
        move_from = self.get_pos()
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            x, y = move_from
            if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if self.can_move(move_from, (x, y), board):
                    moves.append((x, y))
                if board[x][y] is not None:
                    break
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece is not None and piece.is_white() != self.is_white():
                    moves = [cord for cord in moves if cord not in piece.get_possible_moves(board)]
        return moves
