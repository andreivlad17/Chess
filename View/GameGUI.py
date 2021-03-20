import pygame


class GameGUI:
    pygame.init()
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    DIMENSION = 8
    SQUARE_SIZE = WINDOW_HEIGHT // DIMENSION
    PIECES_IMAGES = {}

    MAX_FPS = 15

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        screen.fill(pygame.Color("White"))
        self.loadImages()

    def loadImages(self):
        piecesNames = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP",
                       "wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        for currentPiece in piecesNames:
            self.PIECES_IMAGES[currentPiece] = pygame.image.load("../images/" + currentPiece + ".png")

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
                    screen.blit(self.PIECES_IMAGES[piece],
                                pygame.Rect(column * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE / 2,
                                            self.SQUARE_SIZE / 2))

    def drawGameState(self, screen, gameState):
        self.drawBoard(screen)
        self.drawPieces(screen, gameState.board)




# def main():
#     gameState = GameModel.GameModel()
#     validMoves = gameState.getValidMoves()
#     moveMade = False
#
#     running = True
#     selectedSquare = ()
#     playerClicks = []  # initial piece position, legal move location
#     while running:
#         for currentEvent in pygame.event.get():
#             if currentEvent.type == pygame.QUIT:
#                 running = False
#             elif currentEvent.type == pygame.MOUSEBUTTONDOWN:
#                 mouseClickLocation = pygame.mouse.get_pos()
#                 column = mouseClickLocation[0] // SQUARE_SIZE
#                 row = mouseClickLocation[1] // SQUARE_SIZE
#                 if selectedSquare == (row, column):  # deselect and restart move if the same location is clicked
#                     selectedSquare = ()
#                     playerClicks = []
#                 else:
#                     selectedSquare = (row, column)
#                     playerClicks.append(selectedSquare)
#                 if len(playerClicks) == 2:
#                     move = GameModel.Move(playerClicks[0], playerClicks[1], gameState.board)
#                     if move in validMoves:
#                         gameState.makeMove(move)
#                         moveMade = True
#                         selectedSquare = ()
#                         playerClicks = []
#                     else:
#                         playerClicks = [selectedSquare]
#         if moveMade:
#             validMoves = gameState.getValidMoves()
#             moveMade = False
#
#         drawGameState(screen, gameState)
#         clock.tick(MAX_FPS)
#         pygame.display.flip()
#
#
# main()
