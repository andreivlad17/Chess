from Model.Pieces.Bishop import Bishop
from Model.Pieces.King import King
from Model.Pieces.Knight import Knight
from Model.Pieces.Pawn import Pawn
from Model.Pieces.Queen import Queen
from Model.Pieces.Rook import Rook


class Board:
    squares = []

    def __init__(self):
        self.squares = [
            [Rook("black", (0, 0)), Knight("black", (0, 1)), Bishop("black", (0, 2)), Queen("black", (0, 3)),
             King("black", (0, 4)), Bishop("black", (0, 5)), Knight("black", (0, 6)), Rook("black", (0, 7))],
            [Pawn("black", (1, 0)), Pawn("black", (1, 1)), Pawn("black", (1, 2)), Pawn("black", (1, 3)),
             Pawn("black", (1, 4)), Pawn("black", (1, 5)), Pawn("black", (1, 6)), Pawn("black", (1, 7))],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [Pawn("white", (6, 0)), Pawn("white", (6, 1)), Pawn("white", (6, 2)), Pawn("white", (6, 3)),
             Pawn("white", (6, 4)), Pawn("white", (6, 5)), Pawn("white", (6, 6)), Pawn("white", (6, 7))],
            [Rook("white", (7, 0)), Knight("white", (7, 1)), Bishop("white", (7, 2)), Queen("white", (7, 3)),
             King("white", (7, 4)), Bishop("white", (7, 5)), Knight("white", (7, 6)), Rook("white", (7, 7))],
        ]