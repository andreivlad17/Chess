class InterfaceGameGUI:
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    DIMENSION = 8
    SQUARE_SIZE = WINDOW_HEIGHT // DIMENSION
    PIECES_IMAGES = {}
    MAX_FPS = 15

    def loadImages(self):
        pass

    def drawBoard(self, screen):
        pass

    def drawPieces(self, screen, board):
        pass

    def drawGameState(self, screen, gameState):
        pass

