from piece import Piece


class Knight(Piece):
    def __str__(self):
        return self.color[0].lower() + "N"

    def get_possible_moves(self, *args):
      return []

