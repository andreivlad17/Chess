import pygame

from Model.Game import Game
from Model.Move import Move
from View.InterfaceGameGUI import InterfaceGameGUI


class GameViewPresenter:
    gameView = InterfaceGameGUI

    def __init__(self, view):
        self.gameView = view

    def getGameState(self):
        gameState = Game()
        validMoves = gameState.getValidMoves()
        moveMade = False
        selectedSquare = ()
        playerClicks = []  # initial piece position, legal move location
        running = True

        while running:
            for currentEvent in pygame.event.get():
                if currentEvent.type == pygame.QUIT:
                    running = False
                elif currentEvent.type == pygame.MOUSEBUTTONDOWN:
                    mouseClickLocation = pygame.mouse.get_pos()
                    column = mouseClickLocation[0] // self.gameView.SQUARE_SIZE
                    row = mouseClickLocation[1] // self.gameView.SQUARE_SIZE
                    if selectedSquare == (row, column):  # deselect and restart move if the same location is clicked
                        selectedSquare = ()
                        playerClicks = []
                    else:
                        selectedSquare = (row, column)
                        playerClicks.append(selectedSquare)
                    if len(playerClicks) == 2:
                        move = Move(playerClicks[0], playerClicks[1], gameState.board)
                        if move in validMoves:
                            print(row, column)
                            gameState.makeMove(move)
                            moveMade = True
                            selectedSquare = ()
                            playerClicks = []
                        else:
                            playerClicks = [selectedSquare]
            if moveMade:
                validMoves = gameState.getValidMoves()
                moveMade = False

            self.gameView.drawGameState(self.gameView.screen, gameState, validMoves, selectedSquare)
            self.gameView.clock.tick(self.gameView.MAX_FPS)
            pygame.display.flip()

