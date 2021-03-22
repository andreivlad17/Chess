from Model.Move import Move
from Model.Piece import Piece


class Knight(Piece):
    def getKnightMoves(self, row, column, whiteToMove, board, moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        enemyColor = 'black' if whiteToMove else 'white'
        for currentMove in knightMoves:
            endRow = row + currentMove[0]
            endCol = column + currentMove[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = board[endRow][endCol]
                if (isinstance(endPiece, Piece) and endPiece.color == enemyColor) or endPiece == "--":
                    moves.append(Move((row, column), (endRow, endCol), board))



