from Model.Game import Game
from Model.Move import Move
from Model.Piece import Piece


class King(Piece):
    def getKingMoves(self, row, column):
        kingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        allyColor = 'white' if Game.whiteToMove else 'black'
        for currentMove in range(8):
            endRow = row + kingMoves[currentMove][0]
            endCol = column + kingMoves[currentMove][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = Game.board[endRow][endCol]
                if issubclass(endPiece, Piece) and (endPiece.color is not allyColor):
                    Game.moves.append(Move((row, column), (endRow, endCol), Game.board))
