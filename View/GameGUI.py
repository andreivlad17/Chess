import pygame

from Model.Piece import Piece
from Model.Pieces import Knight
from View.InterfaceGameGUI import InterfaceGameGUI


class GameGUI(InterfaceGameGUI):
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    DIMENSION = 8
    SQUARE_SIZE = WINDOW_HEIGHT // DIMENSION
    PIECES_IMAGES = {}
    MAX_FPS = 15

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self):
        self.screen.fill(pygame.Color("White"))
        self.loadImages()

    def loadImages(self):
        piecesNames = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP",
                       "wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        for currentPiece in piecesNames:
            self.PIECES_IMAGES[currentPiece] = pygame.image.load("./images/" + currentPiece + ".png")

    def drawBoard(self, screen):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                color = colors[((row + column) % 2)]
                pygame.draw.rect(screen, color,
                                 pygame.Rect(column * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE,
                                             self.SQUARE_SIZE))

    def drawPieces(self, screen, board):
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                piece = board[row][column]
                if piece != "--":
                    screen.blit(self.PIECES_IMAGES[self.parsePieceToKey(piece)],
                                pygame.Rect(column * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE / 2,
                                            self.SQUARE_SIZE / 2))

    def drawGameState(self, screen, gameState, validMoves, selectedSquare):
        self.drawBoard(screen)
        self.highlightSquares(screen, gameState, validMoves, selectedSquare)
        self.drawPieces(screen, gameState.board)

    def highlightSquares(self, screen, gameState, validMoves, selectedSquare):
        if selectedSquare != ():
            row, column = selectedSquare
            if isinstance(gameState.board[row][column], Piece) and gameState.board[row][column].color == ("white" if gameState.whiteToMove else "black"):
                selectedSurface = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE))
                selectedSurface.set_alpha(80)
                selectedSurface.fill(pygame.Color("blue"))
                screen.blit(selectedSurface, (column * self.SQUARE_SIZE, row * self.SQUARE_SIZE))

                for currentMove in validMoves:
                    if currentMove.startRow == row and currentMove.startCol == column:
                        selectedSurface.fill(pygame.Color('yellow'))
                        screen.blit(selectedSurface, (currentMove.endCol * self.SQUARE_SIZE, currentMove.endRow * self.SQUARE_SIZE))
                        if isinstance(gameState.board[currentMove.endRow][currentMove.endCol], Piece) and gameState.board[currentMove.endRow][currentMove.endCol].color == ("black" if gameState.whiteToMove else "white"):
                            selectedSurface.fill(pygame.Color('red'))
                            screen.blit(selectedSurface,
                                        (currentMove.endCol * self.SQUARE_SIZE, currentMove.endRow * self.SQUARE_SIZE))


    def parsePieceToKey(self, piece):
        if isinstance(piece, Piece):
            if isinstance(piece, Knight.Knight):
                return piece.color[0] + "N"
            return piece.color[0] + type(piece).__name__[0]
