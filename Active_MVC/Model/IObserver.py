from abc import abstractmethod


class IObserverPiece:
    @abstractmethod
    def update(self):
        pass


class IObserver:
    @abstractmethod
    def update(self, screen, gameState, validMoves, selectedSquare):
        pass

