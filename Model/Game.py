from Model.Piece import Piece
from Model.Board import Board
from Model.Pieces.Queen import Queen
from Model.Pieces.King import King
from Model.Pieces.Rook import Rook
from Model.Pieces.Bishop import Bishop
from Model.Pieces.Knight import Knight
from Model.Pieces.Pawn import Pawn


class Game:
    board = Board.squares
    moves = []
    whiteToMove = True
    moveLog = []
    whiteKingLocation = (7, 4)
    blackKingLocation = (0, 4)
    checkMate = False
    staleMate = False

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.movedPiece
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # switch turns
        if isinstance(move.movedPiece, King):
            if move.movedPiece.color == "white":
                self.whiteKingLocation = (move.endRow, move.endCol)
            elif move.movedPiece.color == "black":
                self.blackKingLocation = (move.endRow, move.endCol)

    def getPossibleMoves(self):
        self.moves = []
        for currentRow in range(len(self.board)):
            for currentColumn in range(len(self.board[currentRow])):
                if isinstance(self.board[currentRow][currentColumn], Piece):
                    turn = self.board[currentRow][currentColumn].color  # get the color for the current turn
                    if (turn == "white" and self.whiteToMove) or (turn == "black" and not self.whiteToMove):
                        pieceType = self.board[currentRow][currentColumn]  # get the piece type
                        if isinstance(pieceType, Pawn):
                            self.board[currentRow][currentColumn].getPawnMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
                        elif isinstance(pieceType, Rook):
                            self.board[currentRow][currentColumn].getRookMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
                        elif isinstance(pieceType, Knight):
                            # print("Before: " + self.moves.index(len(self.moves) - 1).__str__())
                            self.board[currentRow][currentColumn].getKnightMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
                            # print("After: " + self.moves.index(len(self.moves) - 1).__str__())
                        elif isinstance(pieceType, Bishop):
                            self.board[currentRow][currentColumn].getBishopMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
                        elif isinstance(pieceType, Queen):
                            self.board[currentRow][currentColumn].getQueenMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
                        elif isinstance(pieceType, King):
                            self.board[currentRow][currentColumn].getKingMoves(currentRow, currentColumn, self.whiteToMove, self.board, self.moves)
        return self.moves

    def getValidMoves(self):
        moves = self.getPossibleMoves()
        for i in range(len(moves) - 1, -1, -1):
            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        if len(moves) == 0:
            if self.inCheck():
                self.checkMate = True
            else:
                self.staleMate = True
        else:
            self.checkMate = False
            self.staleMate = False

        return moves

    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    def squareUnderAttack(self, row, column):
        self.whiteToMove = not self.whiteToMove
        enemyMoves = self.getPossibleMoves()
        self.whiteToMove = not self.whiteToMove
        for move in enemyMoves:
            if move.endRow == row and move.endCol == column:
                self.whiteToMove = not self.whiteToMove
                return True
        return False

    def undoMove(self):
        if len(self.moves):
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.movedPiece
            self.board[move.endRow][move.endCol] = move.takenPiece
            self.whiteToMove = not self.whiteToMove
            if isinstance(move.movedPiece, King):
                if move.movedPiece.color == "white":
                    self.whiteKingLocation = (move.endRow, move.endCol)
                elif move.movedPiece.color == "black":
                    self.blackKingLocation = (move.endRow, move.endCol)