import random

from MVC.Model.Piece import Piece

pieceScore = {"King": 0, "Queen": 10, "Rook": 5, "Bishop": 3, "Knight": 3, "Pawn": 1}
CHECKMATE_SCORE = 1000
STALEMATE_SCORE = 0
MIN_MAX_DEPTH = 2


def findRandomMove(validMoves):
    return random.choice(validMoves)


def findBestMove(gameState, validMoves):
    currentTurnMultiplier = 1 if gameState.whiteToMove else -1
    opponentMinMaxScore = CHECKMATE_SCORE
    bestPlayerMove = None
    random.shuffle(validMoves)

    for playerMove in validMoves:
        gameState.makeMove(playerMove)
        if gameState.staleMate:
            opponentMaxScore = STALEMATE_SCORE
        elif gameState.checkMate:
            opponentMaxScore = -CHECKMATE_SCORE
        else:
            opponentMoves = gameState.getValidMoves()
            opponentMaxScore = -CHECKMATE_SCORE
            for opponentMove in opponentMoves:
                gameState.makeMove(opponentMove)
                gameState.getValidMoves()
                if gameState.checkMate:
                    score = CHECKMATE_SCORE
                elif gameState.staleMate:
                    score = STALEMATE_SCORE
                else:
                    score = -currentTurnMultiplier * getColorScore(gameState.board)
                if score > opponentMaxScore:
                    opponentMaxScore = score
                gameState.undoMove()
        if opponentMinMaxScore > opponentMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove
        gameState.undoMove()

    return bestPlayerMove


def findBestMoveMinMax(gameState, validMoves):
    global nextMove
    nextMove = None
    random.shuffle(validMoves)
    findMoveMinMax(gameState, validMoves, MIN_MAX_DEPTH, gameState.whiteToMove)
    return nextMove


def findMoveMinMax(gameState, validMoves, depth, whiteToMove):
    global nextMove
    if depth == 0:
        return scoreHeuristic(gameState)

    if whiteToMove:
        maxScore = -CHECKMATE_SCORE
        for validMove in validMoves:
            gameState.makeMove(validMove)
            nextMoves = gameState.getValidMoves()
            score = findMoveMinMax(gameState, nextMoves, depth - 1, False)
            if score > maxScore:
                maxScore = score
                if depth == MIN_MAX_DEPTH:
                    nextMove = validMove
            gameState.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE_SCORE
        for validMove in validMoves:
            gameState.makeMove(validMove)
            nextMoves = gameState.getValidMoves()
            score = findMoveMinMax(gameState, nextMoves, depth - 1, True)
            if score < minScore:
                minScore = score
                if depth == MIN_MAX_DEPTH:
                    nextMove = validMove
            gameState.undoMove()
        return minScore


def scoreHeuristic(gameState):
    if gameState.checkMate:
        if gameState.whiteToMove:
            return -CHECKMATE_SCORE
        else:
            return CHECKMATE_SCORE
    elif gameState.staleMate:
        return STALEMATE_SCORE

    score = 0
    for row in gameState.board:
        for square in row:
            if isinstance(square, Piece) and square.color == "white":
                score += pieceScore[type(square).__name__]
            elif isinstance(square, Piece) and square.color == "black":
                score -= pieceScore[type(square).__name__]

    return score


def getColorScore(board):
    score = 0
    for row in board:
        for square in row:
            if isinstance(square, Piece) and square.color == "white":
                score += pieceScore[type(square).__name__]
            elif isinstance(square, Piece) and square.color == "black":
                score -= pieceScore[type(square).__name__]

    return score
