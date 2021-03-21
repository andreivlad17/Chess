from Model.Move import Move
from Model.Piece import Piece


class Queen(Piece):
    def getQueenMoves(self, row, column, whiteToMove, board, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        enemyColor = 'black' if whiteToMove else 'white'
        for currentDirection in directions:
            for i in range(1, 8):
                endRow = row + currentDirection[0] * i
                endCol = column + currentDirection[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((row, column), (endRow, endCol), board))
                    elif isinstance(endPiece, Piece) and endPiece.color == enemyColor:
                        moves.append(Move((row, column), (endRow, endCol), board))
                        break
                    else:
                        break
                else:
                    break

