import pygame

from Model.Piece import Piece
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

    def drawGameState(self, screen, gameState):
        self.drawBoard(screen)
        self.drawPieces(screen, gameState.board)

    def parsePieceToKey(self, piece):
        if isinstance(piece, Piece):
            if type(piece).__name__ == "Knight":
                return piece.color[0] + 'N'
            return piece.color[0] + type(piece).__name__[0]
