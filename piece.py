class Piece:
    def __init__(self, color: str, position: tuple):
        self.color = color
        self.first_move = True
        self.can_capture = False
        self.position = position

    @property
    def __str__(self) -> str:
        return self.color[0].lower()

    def can_move(self, move_from: tuple, move_to: tuple, board: list[list]) -> bool:
        if not (0 <= move_to[0] < 8 and 0 <= move_to[1] < 8):
            return False
        target_piece = board[move_to[0]][move_to[1]]
        if target_piece is not None and target_piece.is_white() == self.is_white():
            return False
        if not self.is_clear_path(move_from, move_to, board):
            return False
        return True

    def get_pos(self) -> tuple:
        return self.position

    def set_pos(self, new_pos: tuple) -> None:
        self.position = new_pos

    def move(self, new_cord: tuple) -> None:
        self.first_move = False
        self.set_pos(new_cord)

    def is_first_move(self) -> bool:
        return self.first_move

    def is_white(self) -> bool:
        if self.color == "White":
            return True
        return False

    def is_clear_path(self,move_from: tuple, move_to: tuple, board: list[list]) -> bool:
        dx = move_to[0] - move_from[0]
        dy = move_to[1] - move_from[1]
        if dx == 0:
            step = 1 if dy > 0 else -1
            for y in range(move_from[1] + step, move_to[1], step):
                if board[move_from[0]][y] is not None:
                    return False
        elif dy == 0:
            step = 1 if dx > 0 else -1
            for x in range(move_from[0] + step, move_to[0], step):
                if board[x][move_from[1]] is not None:
                    return False
        elif abs(dx) == abs(dy):
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            x, y = move_from[0] + step_x, move_from[1] + step_y
            while (x, y) != move_to:
                if board[x][y] is not None:
                    return False
                x += step_x
                y += step_y
        else:
            return False
        return True


