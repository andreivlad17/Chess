from Model.Move import Move
from Model.Piece import Piece


class Pawn(Piece):
    def getPawnMoves(self, row, column, whiteToMove, board, moves):
        if whiteToMove:  # white's turn
            if board[row - 1][column] == "--":
                moves.append((Move((row, column), (row - 1, column), board)))
                if row == 6 and board[row - 2][column] == "--":
                    moves.append(Move((row, column), (row - 2, column), board))
            # capturing other pieces cases
            if column - 1 >= 0:  # left
                if isinstance(board[row - 1][column - 1], Piece) and board[row - 1][column - 1].color == 'black':
                    moves.append(Move((row, column), (row - 1, column - 1), board))
            if column + 1 <= 7:  # right
                if isinstance(board[row - 1][column + 1], Piece) and board[row - 1][column + 1].color == 'black':
                    moves.append(Move((row, column), (row - 1, column + 1), board))
        else:  # black's turn
            if board[row + 1][column] == "--":
                moves.append((Move((row, column), (row + 1, column), board)))
                if row == 1 and board[row + 2][column] == "--":
                    moves.append(Move((row, column), (row + 2, column), board))
            # capturing other pieces
            if column + 1 <= 7:  # right
                if isinstance(board[row + 1][column + 1], Piece) and board[row + 1][column + 1].color == 'white':
                    moves.append(Move((row, column), (row + 1, column + 1), board))
            if column - 1 >= 0:  # left
                if isinstance(board[row + 1][column - 1], Piece) and board[row + 1][column - 1].color == 'white':
                    moves.append(Move((row, column), (row + 1, column - 1), board))

