import pygame

from MVC.Model import SmartAgent
from MVC.Model.Game import Game
from MVC.Model.Move import Move


class GameController:
    def __init__(self, view, gameModel):
        self.gameView = view
        self.gameState = gameModel

    def getGameState(self):
        validMoves = self.gameState.getValidMoves()
        moveMade = False
        selectedSquare = ()
        playerClicks = []  # initial piece position, legal move location
        running = True
        gameOver = True

        while running:
            humanTurn = (self.gameState.whiteToMove and not self.gameState.whiteAIControl) or (not self.gameState.whiteToMove and not self.gameState.blackAIControl)
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
                            move = Move(playerClicks[0], playerClicks[1], self.gameState.board)
                            if move in validMoves:
                                print(rowClickLocation, columnClickLocation)
                                self.gameState.makeMove(move)
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
                        self.gameState = Game()
                        validMoves = self.gameState.getValidMoves()
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                    elif currentEvent.ui_element == self.gameView.restartGameButton:
                        print("test restart")
                        self.gameState = Game()
                        validMoves = []
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                        self.drawGameState(self.gameView.screen, self.gameState, self.gameState.getValidMoves(), selectedSquare)
                    elif currentEvent.ui_element == self.gameView.pvpButton:
                        print("test pvp")
                        self.gameState.whiteAIControl = False
                        self.gameState.blackAIControl = False
                    elif currentEvent.ui_element == self.gameView.pvAIButton:
                        print("test pve")
                        self.gameState.whiteAIControl = False
                        self.gameState.blackAIControl = True
                    elif currentEvent.ui_element == self.gameView.AIvAIButton:
                        print("test ai")
                        self.gameState.whiteAIControl = True
                        self.gameState.blackAIControl = True
                    self.gameView.manager.process_events(currentEvent)

            if not gameOver and not humanTurn:
                agentMove = SmartAgent.findBestMoveMinMax(self.gameState, validMoves)
                if agentMove is None:
                    agentMove = SmartAgent.findRandomMove(validMoves)
                self.gameState.makeMove(agentMove)
                moveMade = True

            if moveMade:
                self.animateMove(self.gameState.moveLog[-1], self.gameView.screen, self.gameState.board)
                validMoves = self.gameState.getValidMoves()
                moveMade = False

            self.drawGameState(self.gameView.screen, self.gameState, validMoves, selectedSquare)

            if self.gameState.checkMate:
                gameOver = True
                if self.gameState.whiteToMove:
                    self.gameView.drawText(self.gameView.screen, "Black wins")
                else:
                    self.gameView.drawText(self.gameView.screen, "White wins")
            elif self.gameState.staleMate:
                gameOver = True
                self.gameView.drawText(self.gameView.screen, "Stalemate")

            self.gameView.clock.tick(self.gameView.MAX_FPS)
            pygame.display.flip()

    def handleDrawText(self, text):
        font = pygame.font.SysFont("Helvetica", 50, True, False)
        textObject = font.render(text, False, pygame.Color("Black"))
        textLocation = pygame.Rect(0, 0, self.gameView.WINDOW_WIDTH, self.gameView.WINDOW_HEIGHT).move(
            self.gameView.WINDOW_WIDTH / 2 - textObject.get_width() / 2, self.gameView.WINDOW_HEIGHT / 2 - textObject.get_height() / 2)
        self.gameView.drawText(self.gameView.screen, textObject, textLocation)

    def drawPieces(self, screen, board):
        for row in range(self.gameView.DIMENSION):
            for column in range(self.gameView.DIMENSION):
                piece = board[row][column]
                if piece != "--":
                    screen.blit(self.gameView.PIECES_IMAGES[self.gameView.parsePieceToKey(piece)],
                                pygame.Rect(column * self.gameView.SQUARE_SIZE, row * self.gameView.SQUARE_SIZE, self.gameView.SQUARE_SIZE / 2,
                                            self.gameView.SQUARE_SIZE / 2))

    def drawGameState(self, screen, gameState, validMoves, selectedSquare):
        time_delta = self.gameView.clock.tick(60)/1000.0
        self.gameView.manager.update(time_delta)
        self.gameView.screen.blit(self.gameView.background, (0, 0))
        self.gameView.drawBoard(screen)
        self.gameView.highlightSquares(screen, gameState, validMoves, selectedSquare)
        self.drawPieces(screen, gameState.board)
        self.gameView.manager.draw_ui(screen)

    def animateMove(self, move, screen, board):
        global colors
        colors = [pygame.Color("white"), pygame.Color("gray")]
        coords = []
        dRow = move.endRow - move.startRow
        dCol = move.endCol - move.startCol
        framePerSquare = 10
        frameCount = (abs(dRow) + abs(dCol)) * framePerSquare
        for frame in range(frameCount + 1):
            row, column = (move.startRow + dRow * frame / frameCount, move.startCol + dCol * frame / frameCount)
            self.gameView.drawBoard(screen)
            self.drawPieces(screen, board)
            color = colors[(move.endRow + move.endCol) % 2]
            endSquare = pygame.Rect(move.endCol * self.gameView.SQUARE_SIZE, move.endRow * self.gameView.SQUARE_SIZE, self.gameView.SQUARE_SIZE,
                                    self.gameView.SQUARE_SIZE)
            pygame.draw.rect(screen, color, endSquare)
            if move.takenPiece != "--":
                screen.blit(self.gameView.PIECES_IMAGES[self.gameView.parsePieceToKey(move.takenPiece)], endSquare)
            screen.blit(self.gameView.PIECES_IMAGES[self.gameView.parsePieceToKey(move.movedPiece)],
                        pygame.Rect(column * self.gameView.SQUARE_SIZE, row * self.gameView.SQUARE_SIZE, self.gameView.SQUARE_SIZE,
                                    self.gameView.SQUARE_SIZE))
            pygame.display.flip()
            self.gameView.clock.tick(60)