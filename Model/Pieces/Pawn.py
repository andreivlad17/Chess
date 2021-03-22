from Model.Move import Move
from Model.Piece import Piece


class Pawn(Piece):
    def getPawnMoves(self, row, column, whiteToMove, board, moves, pins):
        piecePinned = False
        pinDirection = ()
        for i in range(len(pins)-1, -1, -1):
            if pins[i][0] == row and pins[i][1] == column:
                piecePinned = True
                pinDirection = (pins[i][2], pins[i][3])
                pins.remove(pins[i])
                break

        if whiteToMove:  # white's turn
            if board[row - 1][column] == "--":
                if not piecePinned or pinDirection == (-1, 0):
                    moves.append((Move((row, column), (row - 1, column), board)))
                    if row == 6 and board[row - 2][column] == "--":
                        moves.append(Move((row, column), (row - 2, column), board))
            # capturing other pieces cases
            if column - 1 >= 0:  # left
                if isinstance(board[row - 1][column - 1], Piece) and board[row - 1][column - 1].color == 'black':
                    if not piecePinned or pinDirection == (-1, -1):
                        moves.append(Move((row, column), (row - 1, column - 1), board))
            if column + 1 <= 7:  # right
                if isinstance(board[row - 1][column + 1], Piece) and board[row - 1][column + 1].color == 'black':
                    if not piecePinned or pinDirection == (-1, 1):
                        moves.append(Move((row, column), (row - 1, column + 1), board))

        else:  # black's turn
            if board[row + 1][column] == "--":
                if not piecePinned or pinDirection == (1, 0):
                    moves.append((Move((row, column), (row + 1, column), board)))
                    if row == 1 and board[row + 2][column] == "--":
                        moves.append(Move((row, column), (row + 2, column), board))
            # capturing other pieces
            if column + 1 <= 7:  # right
                if isinstance(board[row + 1][column + 1], Piece) and board[row + 1][column + 1].color == 'white':
                    if not piecePinned or pinDirection == (1, -1):
                        moves.append(Move((row, column), (row + 1, column + 1), board))
            if column - 1 >= 0:  # left
                if isinstance(board[row + 1][column - 1], Piece) and board[row + 1][column - 1].color == 'white':
                    if not piecePinned or pinDirection == (1, 1):
                        moves.append(Move((row, column), (row + 1, column - 1), board))

