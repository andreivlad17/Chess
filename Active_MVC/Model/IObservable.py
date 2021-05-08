from abc import abstractmethod


class IObservable:
    @abstractmethod
    def notify(self, view, screen, gameState, validMoves, selectedSquare):
        pass

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

