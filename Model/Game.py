from Model.Piece import Piece
from Model.Pieces.Board import Board
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

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.movedPiece
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # switch turns

    def getPossibleMoves(self):
        self.moves = []
        for currentRow in range(len(self.board)):
            for currentColumn in range(len(self.board[currentRow])):
                if isinstance(self.board[currentRow][currentColumn], Piece):
                    turn = self.board[currentRow][currentColumn].color  # get the color for the current turn
                    if (turn == "white" and self.whiteToMove) or (turn == "black" and not self.whiteToMove):
                        pieceType = self.board[currentRow][currentColumn].__class__  # get the piece type
                        if isinstance(pieceType, Pawn):
                            self.board[currentRow][currentColumn].getPawnMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Rook):
                            self.board[currentRow][currentColumn].getRookMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Knight):
                            self.board[currentRow][currentColumn].getKnightMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Bishop):
                            self.board[currentRow][currentColumn].getBishopMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, Queen):
                            self.board[currentRow][currentColumn].getQueenMoves(currentRow, currentColumn)
                        elif isinstance(pieceType, King):
                            self.board[currentRow][currentColumn].getKingMoves(currentRow, currentColumn)
        return self.moves

    def getValidMoves(self):
        return self.getPossibleMoves()
