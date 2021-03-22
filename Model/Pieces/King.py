from Model.Move import Move
from Model.Piece import Piece


class King(Piece):
    def getKingMoves(self, row, column, whiteToMove, board, moves):
        kingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        enemyColor = 'black' if whiteToMove else 'white'
        for currentMove in range(8):
            endRow = row + kingMoves[currentMove][0]
            endCol = column + kingMoves[currentMove][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = board[endRow][endCol]
                if (isinstance(endPiece, Piece) and endPiece.color == enemyColor) or endPiece == "--":
                    moves.append(Move((row, column), (endRow, endCol), board))


