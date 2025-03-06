from piece import Piece


class Pawn(Piece):
    def __str__(self) -> str:
        return self.color[0].lower() + "P"

    def get_possible_moves(self, board: list[list]) -> list[tuple]:
        moves = []
        move_from = self.get_pos()
        direction = -1 if self.is_white() else 1
        one_step_forward = (move_from[0] + direction, move_from[1])
        if self.can_move(move_from, one_step_forward, board):
            moves.append(one_step_forward)
        if (self.is_white() and move_from[0] == 6) or (not self.is_white() and move_from[0] == 1):
            two_steps_forward = (move_from[0] + 2 * direction, move_from[1])
            if self.can_move(move_from, two_steps_forward, board):
                moves.append(two_steps_forward)
        for delta_y in [-1, 1]:
            attack_pos = (move_from[0] + direction, move_from[1] + delta_y)
            if self.can_move(move_from, attack_pos, board) and board[attack_pos[0]][attack_pos[1]] is not None:
                moves.append(attack_pos)
        return moves


