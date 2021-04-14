
class Piece:
    color = "white"
    moved = False
    position = ()

    def __init__(self, color, position):
        self.color = color
        self.moved = False
        self.position = position


