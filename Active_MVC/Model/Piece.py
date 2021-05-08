from abc import ABC
from Active_MVC.Model.IObserver import IObserverPiece


class Piece(IObserverPiece, ABC):
    color = "white"
    moved = False
    position = ()

    def __init__(self, color, position):
        self.color = color
        self.moved = False
        self.position = position

    def update(self):
        pass


