# from View import GameGUI as gameGUI
#
# def main():
#     gameGUI = gameGUI()
#     screen = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     clock = p.time.Clock()
#     screen.fill(p.Color("White"))
#     gameState = Engine.GameModel()
#     validMoves = gameState.getValidMoves()
#     moveMade = False
#
#     loadImages()
#
#     running = True
#     selectedSquare = ()
#     playerClicks = []  # initial piece position, legal move location
#     while running:
#         for currentEvent in p.event.get():
#             if currentEvent.type == p.QUIT:
#                 running = False
#             elif currentEvent.type == p.MOUSEBUTTONDOWN:
#                 mouseClickLocation = p.mouse.get_pos()
#                 column = mouseClickLocation[0] // SQUARE_SIZE
#                 row = mouseClickLocation[1] // SQUARE_SIZE
#                 if selectedSquare == (row, column):  # deselect and restart move if the same location is clicked
#                     selectedSquare = ()
#                     playerClicks = []
#                 else:
#                     selectedSquare = (row, column)
#                     playerClicks.append(selectedSquare)
#                 if len(playerClicks) == 2:
#                     move = Engine.Move(playerClicks[0], playerClicks[1], gameState.board)
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
#         p.display.flip()