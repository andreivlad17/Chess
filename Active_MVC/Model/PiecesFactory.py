from Active_MVC.Model.Pieces.Bishop import Bishop
from Active_MVC.Model.Pieces.King import King
from Active_MVC.Model.Pieces.Knight import Knight
from Active_MVC.Model.Pieces.Pawn import Pawn
from Active_MVC.Model.Pieces.Queen import Queen
from Active_MVC.Model.Pieces.Rook import Rook


class PiecesFactory:
    def factory(self, position):
        row, col = position
        color = "black"
        if row == 6 or row == 7:
            color = "white"
        if row == 1 or row == 6:
            return Pawn(color, position)
        else:
            if col == 0 or col == 7:
                return Rook(color, position)
            elif col == 1 or col == 6:
                return Knight(color, position)
            elif col == 2 or col == 5:
                return Bishop(color, position)
            elif col == 3:
                return Queen(color, position)
            elif col == 4:
                return King(color, position)
        return None

