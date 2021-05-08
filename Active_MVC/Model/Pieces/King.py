from abc import ABC
from Active_MVC.Model.Move import Move
from Active_MVC.Model.Piece import Piece


class King(Piece, ABC):
    def update(self):
        print('Observer King reacted to event')

    def updateMoves(self, row, column, whiteToMove, board, moves, whiteKingPos, blackKingPos, pinsAndChecks):
        self.update()
        rowMoves = (-1, -1, -1, 0, 0, 1, 1, 1)
        colMoves = (-1, 0, 1, -1, 1, -1, 0, 1)
        enemyColor = 'black' if whiteToMove else 'white'
        for currentMove in range(8):
            endRow = row + rowMoves[currentMove]
            endCol = column + colMoves[currentMove]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = board[endRow][endCol]
                if (isinstance(endPiece, Piece) and endPiece.color == enemyColor) or endPiece == "--":
                    if enemyColor == "black":
                        whiteKingPos = (endRow, endCol)
                    else:
                        blackKingPos = (endRow, endCol)
                    inCheck, pins, checks = pinsAndChecks
                    if not inCheck:
                        moves.append(Move((row, column), (endRow, endCol), board))
                    if enemyColor == "black":
                        whiteKingPos = (row, column)
                    else:
                        blackKingPos = (row, column)


