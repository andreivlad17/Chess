from MVC.Controller.GameController import GameController
from MVC.View.GameGUI import GameGUI

from MVC.Model.Game import Game

if __name__ == '__main__':
    view = GameGUI()
    model = Game()
    controller = GameController(view, model)
    controller.getGameState()
