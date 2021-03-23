import pygame

from Model import SmartAgent
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
        gameOver = False

        while running:
            humanTurn = (gameState.whiteToMove and gameState.playerOne) or (not gameState.whiteToMove and gameState.playerTwo)
            for currentEvent in pygame.event.get():
                if currentEvent.type == pygame.QUIT:
                    running = False
                elif currentEvent.type == pygame.MOUSEBUTTONDOWN:
                    if not gameOver and humanTurn:
                        columnClickLocation, rowClickLocation = self.gameView.getClickLocation()
                        if selectedSquare == (rowClickLocation, columnClickLocation):  # deselect and restart move if the same location is clicked
                            selectedSquare = ()
                            playerClicks = []
                        else:
                            selectedSquare = (rowClickLocation, columnClickLocation)
                            playerClicks.append(selectedSquare)
                        if len(playerClicks) == 2:
                            move = Move(playerClicks[0], playerClicks[1], gameState.board)
                            if move in validMoves:
                                print(rowClickLocation, columnClickLocation)
                                gameState.makeMove(move)
                                moveMade = True
                                selectedSquare = ()
                                playerClicks = []
                            else:
                                playerClicks = [selectedSquare]

            if not gameOver and not humanTurn:
                agentMove = SmartAgent.findRandomMove(validMoves)
                gameState.makeMove(agentMove)
                moveMade = True

            if moveMade:
                validMoves = gameState.getValidMoves()
                moveMade = False

            self.gameView.drawGameState(self.gameView.screen, gameState, validMoves, selectedSquare)
            self.gameView.clock.tick(self.gameView.MAX_FPS)
            pygame.display.flip()

