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
    inCheck = False
    checkMate = False
    staleMate = False
    pins = []
    checks = []

    playerOne = True
    playerTwo = False

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
                            self.board[currentRow][currentColumn].getPawnMoves(currentRow, currentColumn,
                                                                               self.whiteToMove, self.board, self.moves, self.pins)
                        elif isinstance(pieceType, Rook):
                            self.board[currentRow][currentColumn].getRookMoves(currentRow, currentColumn,
                                                                               self.whiteToMove, self.board, self.moves, self.pins)
                        elif isinstance(pieceType, Knight):
                            self.board[currentRow][currentColumn].getKnightMoves(currentRow, currentColumn,
                                                                                 self.whiteToMove, self.board,
                                                                                 self.moves, self.pins)
                        elif isinstance(pieceType, Bishop):
                            self.board[currentRow][currentColumn].getBishopMoves(currentRow, currentColumn,
                                                                                 self.whiteToMove, self.board,
                                                                                 self.moves, self.pins)
                        elif isinstance(pieceType, Queen):
                            self.board[currentRow][currentColumn].getQueenMoves(currentRow, currentColumn,
                                                                                self.whiteToMove, self.board,
                                                                                self.moves, self.pins)
                        elif isinstance(pieceType, King):
                            self.board[currentRow][currentColumn].getKingMoves(currentRow, currentColumn,
                                                                               self.whiteToMove, self.board, self.moves, self.whiteKingLocation, self.blackKingLocation, self.checkPinsAndChecks())
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
                moves = self.getPossibleMoves()
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
                King.getKingMoves(kingRow, kingCol, self.whiteToMove, self.board, moves)
        else:
            moves = self.getPossibleMoves()

        return moves

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
                endCol = startRow + currentDirection[1] * i
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


