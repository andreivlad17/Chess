from abc import ABC
from typing import List

import pygame

from Active_MVC.Model.IObservable import IObservable
from Active_MVC.Model.Piece import Piece
from Active_MVC.Model.Board import Board
from Active_MVC.Model.Pieces.Queen import Queen
from Active_MVC.Model.Pieces.King import King
from Active_MVC.Model.Pieces.Rook import Rook
from Active_MVC.Model.Pieces.Bishop import Bishop
from Active_MVC.Model.Pieces.Knight import Knight
from Active_MVC.Model.Pieces.Pawn import Pawn
from Active_MVC.View.GameGUI import GameGUI


class Game(IObservable, ABC):
    board = Board.squares
    moves = []
    whiteToMove = True
    moveLog = []
    whiteKingLocation = (7, 4)
    blackKingLocation = (0, 4)
    inCheck = False
    checkMate = False
    staleMate = False
    pins = []
    checks = []
    observersPieces: List[Piece] = []

    whiteAIControl = False
    blackAIControl = False

    def __init__(self, view):
        self.observerView = view
        self.board = Board.squares
        self.moves = []
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.inCheck = False
        self.checkMate = False
        self.staleMate = False
        self.pins = []
        self.checks = []

        self.whiteAIControl = False
        self.blackAIControl = False

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

    def updateMoves(self):
        self.moves = []
        for currentRow in range(len(self.board)):
            for currentColumn in range(len(self.board[currentRow])):
                if isinstance(self.board[currentRow][currentColumn], Piece):
                    turn = self.board[currentRow][currentColumn].color  # get the color for the current turn
                    if (turn == "white" and self.whiteToMove) or (turn == "black" and not self.whiteToMove):
                        pieceType = self.board[currentRow][currentColumn]  # get the piece type
                        if isinstance(pieceType, Pawn):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board, self.moves,
                                                                              self.pins)
                        elif isinstance(pieceType, Rook):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board, self.moves,
                                                                              self.pins)
                        elif isinstance(pieceType, Knight):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board,
                                                                              self.moves, self.pins)
                        elif isinstance(pieceType, Bishop):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board,
                                                                              self.moves, self.pins)
                        elif isinstance(pieceType, Queen):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board,
                                                                              self.moves, self.pins)
                        elif isinstance(pieceType, King):
                            self.board[currentRow][currentColumn].updateMoves(currentRow, currentColumn,
                                                                              self.whiteToMove, self.board, self.moves,
                                                                              self.whiteKingLocation,
                                                                              self.blackKingLocation,
                                                                              self.checkPinsAndChecks())
        return self.moves

    def getValidMoves(self):
        moves = []

        self.inCheck, self.pins, self.checks = self.checkPinsAndChecks()
        if self.whiteToMove:
            kingRow = self.whiteKingLocation[0]
            kingCol = self.whiteKingLocation[1]
        else:
            kingRow = self.blackKingLocation[0]
            kingCol = self.blackKingLocation[1]

        if self.inCheck:
            if len(self.checks) == 1:
                moves = self.updateMoves()
                check = self.checks[0]
                checkRow = check[0]
                checkCol = check[1]
                pieceChecking = self.board[checkRow][checkCol]
                validSquares = []
                if isinstance(pieceChecking, Knight):
                    validSquares = [(checkRow, checkCol)]
                else:
                    for i in range(1, 8):
                        validSquare = (kingRow + check[2] * i, kingCol + check[3] * i)
                        validSquares.append(validSquare)
                        if validSquare[0] == checkRow and validSquare[1] == checkCol:
                            break

                for i in range(len(moves) - 1, -1, -1):
                    if not isinstance(moves[i].movedPiece, King):
                        if not (moves[i].endRow, moves[i].endCol) in validSquares:
                            moves.remove(moves[i])
            else:
                dummyKing = King("black", (0, 1))
                dummyKing.updateMoves(kingRow, kingCol, self.whiteToMove, self.board, moves, self.whiteKingLocation,
                                      self.blackKingLocation, self.checkPinsAndChecks())
        else:
            moves = self.updateMoves()

        if len(moves) == 0:
            if self.isInCheck():
                checkmate = True
            else:
                self.staleMate = True
        else:
            checkmate = False
            stalemate = False

        return moves

    def isInCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    def squareUnderAttack(self, row, column):
        self.whiteToMove = not self.whiteToMove
        enemyMoves = self.updateMoves()
        self.whiteToMove = not self.whiteToMove
        for move in enemyMoves:
            if move.endRow == row and move.endCol == column:
                self.whiteToMove = not self.whiteToMove
                return True
        return False

    def checkPinsAndChecks(self):
        pins = []
        checks = []
        inCheck = False
        if self.whiteToMove:
            enemyColor = "black"
            allyColor = "white"
            startRow = self.whiteKingLocation[0]
            startCol = self.whiteKingLocation[1]
        else:
            enemyColor = "white"
            allyColor = "black"
            startRow = self.blackKingLocation[0]
            startCol = self.blackKingLocation[1]
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for j in range(len(directions)):
            currentDirection = directions[j]
            possiblePin = ()
            for i in range(1, 8):
                endRow = startRow + currentDirection[0] * i
                endCol = startCol + currentDirection[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if isinstance(endPiece, Piece) and endPiece.color == allyColor and not isinstance(endPiece, King):
                        if possiblePin == ():
                            possiblePin = (endRow, endCol, currentDirection[0], currentDirection[1])
                        else:
                            break
                    elif isinstance(endPiece, Piece) and endPiece.color == enemyColor:
                        if (0 <= j <= 3 and isinstance(endPiece, Rook)) or \
                                (4 <= j <= 7 and isinstance(endPiece, Bishop)) or \
                                (i == 1 and isinstance(endPiece, Pawn) and ((enemyColor == "white" and 6 <= j <= 7) or (
                                        enemyColor == "black" and 4 <= j <= 5))) or \
                                isinstance(endPiece, Queen) or (i == 1 and isinstance(endPiece, King)):
                            if possiblePin == ():
                                inCheck = True
                                checks.append((endRow, endCol, currentDirection[0], currentDirection[1]))
                                break
                            else:
                                pins.append(possiblePin)
                                break
                        else:
                            break
                else:
                    break

        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        for currentMove in knightMoves:
            endRow = startRow + currentMove[0]
            endCol = startCol + currentMove[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if isinstance(endPiece, Knight) and endPiece.color == enemyColor:
                    inCheck = True
                    checks.append((endRow, endCol, currentMove[0], currentMove[1]))

        return inCheck, pins, checks

    def undoMove(self):
        if len(self.moveLog):
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.movedPiece
            self.board[move.endRow][move.endCol] = move.takenPiece
            self.whiteToMove = not self.whiteToMove
            if isinstance(move.movedPiece, King):
                if move.movedPiece.color == "white":
                    self.whiteKingLocation = (move.endRow, move.endCol)
                elif move.movedPiece.color == "black":
                    self.blackKingLocation = (move.endRow, move.endCol)

        self.checkMate = False
        self.staleMate = False

    # Observer pattern subject method implementations
    def notify(self, view, screen, gameState, validMoves, selectedSquare):
        # self.observerView.update(screen, gameState, validMoves, selectedSquare)
        time_delta = view.clock.tick(60) / 1000.0
        view.manager.update(time_delta)
        screen.blit(view.background, (0, 0))
        view.drawBoard(screen)
        view.highlightSquares(screen, gameState, validMoves, selectedSquare)
        for row in range(view.DIMENSION):
            for column in range(view.DIMENSION):
                piece = self.board[row][column]
                if piece != "--":
                    screen.blit(view.PIECES_IMAGES[view.parsePieceToKey(piece)],
                                pygame.Rect(column * view.SQUARE_SIZE, row * view.SQUARE_SIZE,
                                            view.SQUARE_SIZE / 2,
                                            view.SQUARE_SIZE / 2))
        view.manager.draw_ui(screen)
        for observer in self.observersPieces:
            observer.update()

    def attach(self, observer):
        self.observersPieces.append(observer)

    def detach(self, observer):
        self.observersPieces.remove(observer)
