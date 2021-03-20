from Model.GameModel import GameModel
from Model.Move import Move
from Model.Piece import Piece


class Knight(Piece):
    def getKnightMoves(self, row, column):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColor = 'white' if GameModel.whiteToMove else 'black'
        for currentMove in knightMoves:
            endRow = row + currentMove[0]
            endCol = column + currentMove[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = GameModel.board[endRow][endCol]
                if issubclass(endPiece, Piece) and endPiece.color is not allyColor:
                    GameModel.moves.append(Move((row, column), (endRow, endCol), GameModel.board))
