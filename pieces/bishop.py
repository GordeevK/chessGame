from piece import Piece


class Bishop(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "B"

    def get_possible_moves(self, board: list[list]) -> list[tuple]:
        moves = []
        move_from = self.get_pos()
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            x, y = move_from
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if self.can_move(move_from, (x, y), board):
                    moves.append((x, y))
                if board[x][y] is not None:
                    break
        return moves