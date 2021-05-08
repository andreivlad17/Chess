from Active_MVC.Model.Pieces.Bishop import Bishop
from Active_MVC.Model.Pieces.King import King
from Active_MVC.Model.Pieces.Knight import Knight
from Active_MVC.Model.Pieces.Pawn import Pawn
from Active_MVC.Model.Pieces.Queen import Queen
from Active_MVC.Model.Pieces.Rook import Rook
from Active_MVC.Model.PiecesFactory import PiecesFactory


class Board:
    piecesFactory = PiecesFactory()

    squares = [
            [piecesFactory.factory((0, 0)), piecesFactory.factory((0, 1)), piecesFactory.factory((0, 2)), piecesFactory.factory((0, 3)),
             piecesFactory.factory((0, 4)), piecesFactory.factory((0, 5)), piecesFactory.factory((0, 6)), piecesFactory.factory((0, 7))],
            [piecesFactory.factory((1, 0)), piecesFactory.factory((1, 1)), piecesFactory.factory((1, 2)), piecesFactory.factory((1, 3)),
             piecesFactory.factory((1, 4)), piecesFactory.factory((1, 5)), piecesFactory.factory((1, 6)), piecesFactory.factory((1, 7))],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [piecesFactory.factory((6, 0)), piecesFactory.factory((6, 1)), piecesFactory.factory((6, 2)), piecesFactory.factory((6, 3)),
             piecesFactory.factory((6, 4)), piecesFactory.factory((6, 5)), piecesFactory.factory((6, 6)), piecesFactory.factory((6, 7))],
            [piecesFactory.factory((7, 0)), piecesFactory.factory((7, 1)), piecesFactory.factory((7, 2)), piecesFactory.factory((7, 3)),
             piecesFactory.factory((7, 4)), piecesFactory.factory((7, 5)), piecesFactory.factory((7, 6)), piecesFactory.factory((7, 7))],
        ]

    def __init__(self):
        self.squares = [
            [self.piecesFactory.factory((0, 0)), self.piecesFactory.factory((0, 1)), self.piecesFactory.factory((0, 2)), self.piecesFactory.factory((0, 3)),
             self.piecesFactory.factory((0, 4)), self.piecesFactory.factory((0, 5)), self.piecesFactory.factory((0, 6)), self.piecesFactory.factory((0, 7))],
            [self.piecesFactory.factory((1, 0)), self.piecesFactory.factory((1, 1)), self.piecesFactory.factory((1, 2)), self.piecesFactory.factory((1, 3)),
             self.piecesFactory.factory((1, 4)), self.piecesFactory.factory((1, 5)), self.piecesFactory.factory((1, 6)), self.piecesFactory.factory((1, 7))],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [self.piecesFactory.factory((6, 0)), self.piecesFactory.factory((6, 1)), self.piecesFactory.factory((6, 2)), self.piecesFactory.factory((6, 3)),
             self.piecesFactory.factory((6, 4)), self.piecesFactory.factory((6, 5)), self.piecesFactory.factory((6, 6)), self.piecesFactory.factory((6, 7))],
            [self.piecesFactory.factory((7, 0)), self.piecesFactory.factory((7, 1)), self.piecesFactory.factory((7, 2)), self.piecesFactory.factory((7, 3)),
             self.piecesFactory.factory((7, 4)), self.piecesFactory.factory((7, 5)), self.piecesFactory.factory((7, 6)), self.piecesFactory.factory((7, 7))],
        ]


