import pygame as p
from Model import Engine

p.init()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
DIMENSION = 8
SQUARE_SIZE = WINDOW_HEIGHT // DIMENSION
PIECES_IMAGES = {}

MAX_FPS = 15


def loadImages():
    piecesNames = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP",
                   "wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    for currentPiece in piecesNames:
        PIECES_IMAGES[currentPiece] = p.image.load("../images/" + currentPiece + ".png")


def main():
    p.init()
    screen = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gameState = Engine.GameState()
    validMoves = gameState.getValidMoves()
    moveMade = False

    loadImages()

    running = True
    selectedSquare = ()
    playerClicks = []  # initial piece position, legal move location
    while running:
        for currentEvent in p.event.get():
            if currentEvent.type == p.QUIT:
                running = False
            elif currentEvent.type == p.MOUSEBUTTONDOWN:
                mouseClickLocation = p.mouse.get_pos()
                column = mouseClickLocation[0] // SQUARE_SIZE
                row = mouseClickLocation[1] // SQUARE_SIZE
                if selectedSquare == (row, column):  # deselect and restart move if the same location is clicked
                    selectedSquare = ()
                    playerClicks = []
                else:
                    selectedSquare = (row, column)
                    playerClicks.append(selectedSquare)
                if len(playerClicks) == 2:
                    move = Engine.Move(playerClicks[0], playerClicks[1], gameState.board)
                    if move in validMoves:
                        gameState.makeMove(move)
                        moveMade = True
                        selectedSquare = ()
                        playerClicks = []
                    else:
                        playerClicks = [selectedSquare]
        if moveMade:
            validMoves = gameState.getValidMoves()
            moveMade = False

        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(PIECES_IMAGES[piece],
                            p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawGameState(screen, gameState):
    drawBoard(screen)
    drawPieces(screen, gameState.board)


main()
