from Model.GameModel import GameModel
from Model.Move import Move
from Model.Piece import Piece


class Queen(Piece):
    def getQueenMoves(self, row, column):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        enemyColor = 'black' if GameModel.whiteToMove else 'white'
        for currentDirection in directions:
            for i in range(1, 8):
                endRow = row + currentDirection[0] * i
                endCol = column + currentDirection[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = GameModel.board[endRow][endCol]
                    if endPiece == "--":
                        GameModel.moves.append(Move((row, column), (endRow, endCol), GameModel.board))
                    elif issubclass(endPiece, Piece) and endPiece.color == enemyColor:
                        GameModel.moves.append(Move((row, column), (endRow, endCol), GameModel.board))
                        break
                    else:
                        break
                else:
                    break

