import pygame
import pygame_gui

from MVC.Model.Piece import Piece
from MVC.Model.Pieces import Knight

class GameGUI():
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    DIMENSION = 8
    SQUARE_SIZE = WINDOW_HEIGHT // DIMENSION
    PIECES_IMAGES = {}
    MAX_FPS = 15

    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((WINDOW_WIDTH + 200, WINDOW_HEIGHT))
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#edebe4'))
    manager = pygame_gui.UIManager((800, 600))
    clock = pygame.time.Clock()

    startGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 180), (100, 50)), text='START', manager=manager)
    restartGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 380), (100, 50)), text='RESTART', manager=manager)
    pvpButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((615, 280), (50, 50)), text='PvP', manager=manager)
    pvAIButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((675, 280), (50, 50)), text='PvAI', manager=manager)
    AIvAIButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((735, 280), (50, 50)), text='AIvAI', manager=manager)

    def __init__(self):
        self.screen.fill(pygame.Color("White"))
        self.loadImages()

    def loadImages(self):
        piecesNames = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP",
                       "wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        for currentPiece in piecesNames:
            self.PIECES_IMAGES[currentPiece] = pygame.image.load("../images/" + currentPiece + ".png")

    def drawBoard(self, screen):
        global colors
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                color = colors[((row + column) % 2)]
                pygame.draw.rect(screen, color,
                                 pygame.Rect(column * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE,
                                             self.SQUARE_SIZE))

    def highlightSquares(self, screen, gameState, validMoves, selectedSquare):
        if selectedSquare != () :
            row, column = selectedSquare
            if 0 <= row <= 7 and 0 <= column <= 7:
                if isinstance(gameState.board[row][column], Piece) and gameState.board[row][column].color == (
                        "white" if gameState.whiteToMove else "black"):
                    selectedSurface = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE))
                    selectedSurface.set_alpha(80)
                    selectedSurface.fill(pygame.Color("blue"))
                    screen.blit(selectedSurface, (column * self.SQUARE_SIZE, row * self.SQUARE_SIZE))

                    for currentMove in validMoves:
                        if currentMove.startRow == row and currentMove.startCol == column:
                            selectedSurface.fill(pygame.Color('yellow'))
                            screen.blit(selectedSurface,
                                        (currentMove.endCol * self.SQUARE_SIZE, currentMove.endRow * self.SQUARE_SIZE))
                            if isinstance(gameState.board[currentMove.endRow][currentMove.endCol], Piece) and \
                                    gameState.board[currentMove.endRow][currentMove.endCol].color == (
                                    "black" if gameState.whiteToMove else "white"):
                                selectedSurface.fill(pygame.Color('red'))
                                screen.blit(selectedSurface,
                                            (currentMove.endCol * self.SQUARE_SIZE, currentMove.endRow * self.SQUARE_SIZE))

    def drawText(self, screen, textObject, textLocation):
        screen.blit(textObject, textLocation)

    def parsePieceToKey(self, piece):
        if isinstance(piece, Piece):
            if isinstance(piece, Knight.Knight):
                return piece.color[0] + "N"
            return piece.color[0] + type(piece).__name__[0]

    def getClickLocation(self):
        mouseClickLocation = pygame.mouse.get_pos()
        columnClickLocation = mouseClickLocation[0] // self.SQUARE_SIZE
        rowClickLocation = mouseClickLocation[1] // self.SQUARE_SIZE
        return columnClickLocation, rowClickLocation
