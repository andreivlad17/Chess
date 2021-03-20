from Model.Game import Game
from Model.Move import Move
from Model.Piece import Piece


class Pawn(Piece):
    def getPawnMoves(self, row, column):
        if Game.whiteToMove:  # white's turn
            if Game.board[row - 1][column] == "--":
                Game.moves.append((Move((row, column), (row - 1, column), Game.board)))
                if row == 6 and Game.board[row - 2][column] == "--":
                    Game.moves.append(Move((row, column), (row - 2, column), Game.board))
            # capturing other pieces cases
            if column - 1 >= 0:  # left
                if issubclass(Game.board[row - 1][column - 1], Piece) and Game.board[row - 1][column - 1].color == 'black':
                    Game.moves.append(Move((row, column), (row - 1, column - 1), Game.board))
            if column + 1 <= 7:  # right
                if issubclass(Game.board[row - 1][column + 1], Piece) and Game.board[row - 1][column + 1].color == 'black':
                    Game.moves.append(Move((row, column), (row - 1, column + 1), Game.board))
        else:  # black's turn
            if Game.board[row + 1][column] == "--":
                Game.moves.append((Move((row, column), (row + 1, column), Game.board)))
                if row == 1 and Game.board[row + 2][column] == "--":
                    Game.moves.append(Move((row, column), (row + 2, column), Game.board))
            # capturing other pieces
            if column + 1 <= 7:  # right
                if issubclass(Game.board[row + 1][column + 1], Piece) and Game.board[row + 1][column + 1].color == 'white':
                    Game.moves.append(Move((row, column), (row + 1, column + 1), Game.board))
            if column - 1 >= 0:  # left
                if issubclass(Game.board[row + 1][column - 1], Piece) and Game.board[row + 1][column - 1].color == 'white':
                    Game.moves.append(Move((row, column), (row + 1, column - 1), Game.board))

