from Model.Game import Game
from Model.Move import Move
from Model.Piece import Piece


class Bishop(Piece):
    def getBishopMoves(self, row, column):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        enemyColor = 'black' if Game.whiteToMove else 'white'
        for currentDirection in directions:
            for i in range(1, 8):
                endRow = row + currentDirection[0] * i
                endCol = column + currentDirection[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = Game.board[endRow][endCol]
                    if endPiece == "--":
                        Game.moves.append(Move((row, column), (endRow, endCol), Game.board))
                    elif issubclass(endPiece, Piece) and endPiece.color == enemyColor:
                        Game.moves.append(Move((row, column), (endRow, endCol), Game.board))
                        break
                    else:
                        break
                else:
                    break
