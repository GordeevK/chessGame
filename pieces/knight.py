from piece import Piece


class Knight(Piece):
    def __str__(self):
        return self.color[0].lower() + "N"

    def get_possible_moves(self, board: list[list]) -> list[tuple[int, int]]:
        moves = []
        move_from = self.get_pos()
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dx, dy in directions:
            x, y = move_from
            if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if board[x][y] is None or board[x][y].is_white() != self.is_white():
                    moves.append((x, y))
        return moves
