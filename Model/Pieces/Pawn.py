from Model.GameModel import GameModel
from Model.Move import Move
from Model.Piece import Piece


class Pawn(Piece):
    def getPawnMoves(self, row, column):
        if GameModel.whiteToMove:  # white's turn
            if GameModel.board[row - 1][column] == "--":
                GameModel.moves.append((Move((row, column), (row - 1, column), GameModel.board)))
                if row == 6 and GameModel.board[row - 2][column] == "--":
                    GameModel.moves.append(Move((row, column), (row - 2, column), GameModel.board))
            # capturing other pieces cases
            if column - 1 >= 0:  # left
                if issubclass(GameModel.board[row - 1][column - 1], Piece) and GameModel.board[row - 1][column - 1].color == 'black':
                    GameModel.moves.append(Move((row, column), (row - 1, column - 1), GameModel.board))
            if column + 1 <= 7:  # right
                if issubclass(GameModel.board[row - 1][column + 1], Piece) and GameModel.board[row - 1][column + 1].color == 'black':
                    GameModel.moves.append(Move((row, column), (row - 1, column + 1), GameModel.board))
        else:  # black's turn
            if GameModel.board[row + 1][column] == "--":
                GameModel.moves.append((Move((row, column), (row + 1, column), GameModel.board)))
                if row == 1 and GameModel.board[row + 2][column] == "--":
                    GameModel.moves.append(Move((row, column), (row + 2, column), GameModel.board))
            # capturing other pieces
            if column + 1 <= 7:  # right
                if issubclass(GameModel.board[row + 1][column + 1], Piece) and GameModel.board[row + 1][column + 1].color == 'white':
                    GameModel.moves.append(Move((row, column), (row + 1, column + 1), GameModel.board))
            if column - 1 >= 0:  # left
                if issubclass(GameModel.board[row + 1][column - 1], Piece) and GameModel.board[row + 1][column - 1].color == 'white':
                    GameModel.moves.append(Move((row, column), (row + 1, column - 1), GameModel.board))

