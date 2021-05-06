import pygame
import xml.etree.ElementTree as ET

from MVC.Model import SmartAgent
from MVC.Model.Game import Game
from MVC.Model.Move import Move


class GameController:
    def __init__(self, view, gameModel):
        self.gameView = view
        self.gameState = gameModel

    def getGameState(self):
        languageXmlTree = ET.parse('../Config/languages.xml')
        languagesRoot = languageXmlTree.getroot()
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

                    # Side button handlers
                    if self.gameView.startGameButton.rect.collidepoint(currentEvent.pos):
                        print("test start")
                        gameOver = False
                        self.gameState = Game()
                        validMoves = self.gameState.getValidMoves()
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                    elif self.gameView.restartGameButton.rect.collidepoint(currentEvent.pos):
                        print("test restart")
                        self.gameState = Game()
                        validMoves = []
                        selectedSquare = ()
                        playerClicks = []
                        moveMade = False
                        self.drawGameState(self.gameView.screen, self.gameState, self.gameState.getValidMoves(), selectedSquare)
                    elif self.gameView.pvpButton.rect.collidepoint(currentEvent.pos):
                        print("test pvp")
                        self.gameState.whiteAIControl = False
                        self.gameState.blackAIControl = False
                    elif self.gameView.pvAIButton.rect.collidepoint(currentEvent.pos):
                        print("test pve")
                        self.gameState.whiteAIControl = False
                        self.gameState.blackAIControl = True
                    elif self.gameView.AIvAIButton.rect.collidepoint(currentEvent.pos):
                        print("test ai")
                        self.gameState.whiteAIControl = True
                        self.gameState.blackAIControl = True
                    elif self.gameView.lang_ro.rect.collidepoint(currentEvent.pos):
                        print("test ro")
                        for language in languagesRoot.findall("language"):
                            if language.get('name') == "romanian":
                                romanian = language
                                break
                        self.gameView.startGameButton.set_text(romanian.find('start').text)
                        self.gameView.restartGameButton.set_text(romanian.find('restart').text)
                        self.gameView.pvpButton.set_text(romanian.find('pvp').text)
                        self.gameView.pvAIButton.set_text(romanian.find('pvai').text)
                        self.gameView.AIvAIButton.set_text(romanian.find('aivai').text)
                    elif self.gameView.lang_en.rect.collidepoint(currentEvent.pos):
                        print("test en")
                        english = None
                        for language in languagesRoot.findall("language"):
                            if language.get('name') == "english":
                                english = language
                                break
                        self.gameView.startGameButton.set_text(english.find('start').text)
                        self.gameView.restartGameButton.set_text(english.find('restart').text)
                        self.gameView.pvpButton.set_text(english.find('pvp').text)
                        self.gameView.pvAIButton.set_text(english.find('pvai').text)
                        self.gameView.AIvAIButton.set_text(english.find('aivai').text)
                    elif self.gameView.lang_fr.rect.collidepoint(currentEvent.pos):
                        print("test fr")
                        french = None
                        for language in languagesRoot.findall("language"):
                            if language.get('name') == "french":
                                french = language
                                break
                        self.gameView.startGameButton.set_text(french.find('start').text)
                        self.gameView.restartGameButton.set_text(french.find('restart').text)
                        self.gameView.pvpButton.set_text(french.find('pvp').text)
                        self.gameView.pvAIButton.set_text(french.find('pvai').text)
                        self.gameView.AIvAIButton.set_text(french.find('aivai').text)
                    elif self.gameView.lang_ch.rect.collidepoint(currentEvent.pos):
                        print("test ch")
                        chinese = None
                        for language in languagesRoot.findall("language"):
                            if language.get('name') == "chinese":
                                chinese = language
                                break
                        self.gameView.startGameButton.set_text(chinese.find('start').text)
                        self.gameView.restartGameButton.set_text(chinese.find('restart').text)
                        self.gameView.pvpButton.set_text(chinese.find('pvp').text)
                        self.gameView.pvAIButton.set_text(chinese.find('pvai').text)
                        self.gameView.AIvAIButton.set_text(chinese.find('aivai').text)
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