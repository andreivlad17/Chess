from abc import ABC
from Active_MVC.Model.Move import Move
from Active_MVC.Model.Piece import Piece


class Knight(Piece, ABC):
    def update(self):
        print('Observer Knight reacted to event')

    def updateMoves(self, row, column, whiteToMove, board, moves, pins):
        self.update()
        piecePinned = False
        pinDirection = ()
        for i in range(len(pins) - 1, -1, -1):
            if pins[i][0] == row and pins[i][1] == column:
                piecePinned = True
                pinDirection = (pins[i][2], pins[i][3])
                pins.remove(pins[i])
                break

        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        enemyColor = 'black' if whiteToMove else 'white'
        for currentMove in knightMoves:
            endRow = row + currentMove[0]
            endCol = column + currentMove[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                if not piecePinned:
                    endPiece = board[endRow][endCol]
                    if (isinstance(endPiece, Piece) and endPiece.color == enemyColor) or endPiece == "--":
                        moves.append(Move((row, column), (endRow, endCol), board))



