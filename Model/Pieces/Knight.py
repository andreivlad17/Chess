from Model.Game import Game
from Model.Move import Move
from Model.Piece import Piece


class Knight(Piece):
    def getKnightMoves(self, row, column):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColor = 'white' if Game.whiteToMove else 'black'
        for currentMove in knightMoves:
            endRow = row + currentMove[0]
            endCol = column + currentMove[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = Game.board[endRow][endCol]
                if issubclass(endPiece, Piece) and endPiece.color is not allyColor:
                    Game.moves.append(Move((row, column), (endRow, endCol), Game.board))
