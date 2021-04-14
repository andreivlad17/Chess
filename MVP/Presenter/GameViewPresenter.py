import pygame
import pygame_gui

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
        gameOver = True

        while running:
            humanTurn = (gameState.whiteToMove and not gameState.whiteAIControl) or (not gameState.whiteToMove and not gameState.blackAIControl)
            for currentEvent in pygame.event.get():
                if currentEvent.type == pygame.QUIT:
                    running = False
                if currentEvent.type == pygame.MOUSEBUTTONDOWN:
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
                if currentEvent.type == pygame.USEREVENT:
                    #if currentEvent.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    print("test button")

                    if currentEvent.ui_element == self.gameView.startGameButton:
                        print("test start")
                        gameOver = False
                        gameState = Game()
                        validMoves = gameState.getValidMoves()
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                    elif currentEvent.ui_element == self.gameView.restartGameButton:
                        print("test restart")
                        gameState = Game()
                        validMoves = gameState.getValidMoves()
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                    elif currentEvent.ui_element == self.gameView.pvpButton:
                        print("test pvp")
                        gameState.whiteAIControl = False
                        gameState.blackAIControl = False
                    elif currentEvent.ui_element == self.gameView.pvAIButton:
                        print("test pve")
                        gameState.whiteAIControl = False
                        gameState.blackAIControl = True
                    elif currentEvent.ui_element == self.gameView.AIvAIButton:
                        print("test ai")
                        gameState.whiteAIControl = True
                        gameState.blackAIControl = True
                    self.gameView.manager.process_events(currentEvent)

            if not gameOver and not humanTurn:
                agentMove = SmartAgent.findBestMoveMinMax(gameState, validMoves)
                if agentMove is None:
                    agentMove = SmartAgent.findRandomMove(validMoves)
                gameState.makeMove(agentMove)
                moveMade = True

            if moveMade:
                self.gameView.animateMove(gameState.moveLog[-1], self.gameView.screen, gameState.board)
                validMoves = gameState.getValidMoves()
                moveMade = False

            self.gameView.drawGameState(self.gameView.screen, gameState, validMoves, selectedSquare)

            if gameState.checkMate:
                gameOver = True
                if gameState.whiteToMove:
                    self.gameView.drawText(self.gameView.screen, "Black wins")
                else:
                    self.gameView.drawText(self.gameView.screen, "White wins")
            elif gameState.staleMate:
                gameOver = True
                self.gameView.drawText(self.gameView.screen, "Stalemate")

            self.gameView.clock.tick(self.gameView.MAX_FPS)
            pygame.display.flip()

