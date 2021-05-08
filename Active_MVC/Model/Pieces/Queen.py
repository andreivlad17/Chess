from abc import ABC
from Active_MVC.Model.Move import Move
from Active_MVC.Model.Piece import Piece


class Queen(Piece, ABC):
    def update(self):
        print('Observer Queen reacted to event')

    def updateMoves(self, row, column, whiteToMove, board, moves, pins):
        self.update()
        piecePinned = False
        pinDirection = ()
        for i in range(len(pins) - 1, -1, -1):
            if pins[i][0] == row and pins[i][1] == column:
                piecePinned = True
                pinDirection = (pins[i][2], pins[i][3])
                if not isinstance(board[row][column], Queen):
                    pins.remove(pins[i])
                break

        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        enemyColor = 'black' if whiteToMove else 'white'
        for currentDirection in directions:
            for i in range(1, 8):
                endRow = row + currentDirection[0] * i
                endCol = column + currentDirection[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    if not piecePinned or pinDirection == currentDirection or pinDirection == (
                    -currentDirection[0], -currentDirection[1]):
                        endPiece = board[endRow][endCol]
                        if endPiece == "--":
                            moves.append(Move((row, column), (endRow, endCol), board))
                        elif isinstance(endPiece, Piece) and endPiece.color == enemyColor:
                            moves.append((Move((row, column), (endRow, endCol), board)))
                            break
                        else:
                            break
                else:
                    break

