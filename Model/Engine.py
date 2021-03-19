class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.movedPiece
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # switch turns

    def getValidMoves(self):
        return self.getPossibleMoves()

    def getPossibleMoves(self):
        moves = []
        for currentRow in range(len(self.board)):
            for currentColumn in range(len(self.board[currentRow])):
                turn = self.board[currentRow][currentColumn][0]  # get the color for the current turn
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[currentRow][currentColumn][1]  # get the piece type
                    if piece == 'P':
                        self.getPawnMoves(currentRow, currentColumn, moves)
                    elif piece == 'R':
                        self.getRookMoves(currentRow, currentColumn, moves)
                    elif piece == 'N':
                        self.getKnightMoves(currentRow, currentColumn, moves)
                    elif piece == 'B':
                        self.getBishopMoves(currentRow, currentColumn, moves)
                    elif piece == 'Q':
                        self.getQueenMoves(currentRow, currentColumn, moves)
                    elif piece == 'K':
                        self.getKingMoves(currentRow, currentColumn, moves)
        return moves

    def getPawnMoves(self, row, column, moves):
        if self.whiteToMove:  # white's turn
            if self.board[row - 1][column] == "--":
                moves.append((Move((row, column), (row - 1, column), self.board)))
                if row == 6 and self.board[row - 6][column] == "--":
                    moves.append(Move((row, column), (row - 2, column), self.board))
            # capturing other pieces cases
            if column - 1 >= 0:  # left
                if self.board[row - 1][column - 1][0] == 'b':
                    moves.append(Move((row, column), (row - 1, column - 1), self.board))
            if column + 1 <= 7:  # right
                if self.board[row - 1][column + 1][0] == 'b':
                    moves.append(Move((row, column), (row - 1, column + 1), self.board))
        else:  # black's turn
            if self.board[row + 1][column] == "--":
                moves.append((Move((row, column), (row + 1, column), self.board)))
                if row == 6 and self.board[row + 6][column] == "--":
                    moves.append(Move((row, column), (row + 2, column), self.board))
            if column + 1 <= 7:  # right
                if self.board[row + 1][column + 1][0] == 'w':
                    moves.append(Move((row, column), (row + 1, column + 1), self.board))
            if column - 1 >= 0:  # left
                if self.board[row + 1][column - 1][0] == 'w':
                    moves.append(Move((row, column), (row + 1, column - 1), self.board))

    def getRookMoves(self, row, column, moves):
        pass

    def getKnightMoves(self, row, column, moves):
        pass

    def getBishopMoves(self, row, column, moves):
        pass

    def getQueenMoves(self, row, column, moves):
        pass

    def getKingMoves(self, row, column, moves):
        pass


class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in ranksToRows.items()}

    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.movedPiece = board[self.startRow][self.startCol]
        self.takenPiece = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, column):
        return self.colsToFiles[column] + self.rowsToRanks[row]
