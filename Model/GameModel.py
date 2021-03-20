from Model.Piece import Piece
from Model.Pieces.Queen import Queen
from Model.Pieces.King import King
from Model.Pieces.Rook import Rook
from Model.Pieces.Bishop import Bishop
from Model.Pieces.Knight import Knight
from Model.Pieces.Pawn import Pawn


class GameModel:
    board = []
    moves = []
    whiteToMove = True
    moveLog = []

    def __init__(self):
        self.board = [
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

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.movedPiece
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # switch turns

    def getPossibleMoves(self):
        self.moves = []
        for currentRow in range(len(self.board)):
            for currentColumn in range(len(self.board[currentRow])):
                if isinstance(self.board[currentRow][currentColumn], Piece):
                    turn = self.board[currentRow][currentColumn].color  # get the color for the current turn
                    if (turn == "white" and self.whiteToMove) or (turn == "black" and not self.whiteToMove):
                        pieceType = self.board[currentRow][currentColumn].__class__  # get the piece type
                        if isinstance(pieceType, Pawn):
                            self.board[currentRow][currentColumn].getPawnMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Rook):
                            self.board[currentRow][currentColumn].getRookMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Knight):
                            self.board[currentRow][currentColumn].getKnightMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Bishop):
                            self.board[currentRow][currentColumn].getBishopMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Queen):
                            self.board[currentRow][currentColumn].getQueenMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, King):
                            self.board[currentRow][currentColumn].getKingMoves(currentRow, currentColumn)
        return self.moves

    def getValidMoves(self):
        return self.getPossibleMoves()
