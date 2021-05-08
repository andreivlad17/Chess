from abc import ABC
from Active_MVC.Model.Move import Move
from Active_MVC.Model.Piece import Piece


class Pawn(Piece, ABC):
    def update(self):
        print('Observer Pawn reacted to event')

    def updateMoves(self, row, column, whiteToMove, board, moves, pins):
        self.update()
        piecePinned = False
        pinDirection = ()
        for i in range(len(pins)-1, -1, -1):
            if pins[i][0] == row and pins[i][1] == column:
                piecePinned = True
                pinDirection = (pins[i][2], pins[i][3])
                pins.remove(pins[i])
                break

        if whiteToMove:  # white's turn
            if row > 0 and board[row - 1][column] == "--":
                if not piecePinned or pinDirection == (-1, 0):
                    moves.append((Move((row, column), (row - 1, column), board)))
                    if row == 6 and board[row - 2][column] == "--":
                        moves.append(Move((row, column), (row - 2, column), board))
            # capturing other pieces cases
            if row > 0 and column - 1 >= 0:  # left
                if isinstance(board[row - 1][column - 1], Piece) and board[row - 1][column - 1].color == 'black':
                    if not piecePinned or pinDirection == (-1, -1):
                        moves.append(Move((row, column), (row - 1, column - 1), board))
            if row > 0 and column + 1 <= 7:  # right
                if isinstance(board[row - 1][column + 1], Piece) and board[row - 1][column + 1].color == 'black':
                    if not piecePinned or pinDirection == (-1, 1):
                        moves.append(Move((row, column), (row - 1, column + 1), board))

        else:  # black's turn
            if row < 7 and board[row + 1][column] == "--":
                if not piecePinned or pinDirection == (1, 0):
                    moves.append((Move((row, column), (row + 1, column), board)))
                    if row == 1 and board[row + 2][column] == "--":
                        moves.append(Move((row, column), (row + 2, column), board))
            # capturing other pieces
            if row < 7 and column + 1 <= 7:  # right
                if isinstance(board[row + 1][column + 1], Piece) and board[row + 1][column + 1].color == 'white':
                    if not piecePinned or pinDirection == (1, -1):
                        moves.append(Move((row, column), (row + 1, column + 1), board))
            if row < 7 and column - 1 >= 0:  # left
                if isinstance(board[row + 1][column - 1], Piece) and board[row + 1][column - 1].color == 'white':
                    if not piecePinned or pinDirection == (1, 1):
                        moves.append(Move((row, column), (row + 1, column - 1), board))
