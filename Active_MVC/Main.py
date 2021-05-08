from Active_MVC.Controller.GameController import GameController
from Active_MVC.View.GameGUI import GameGUI

from Active_MVC.Model.Game import Game

if __name__ == '__main__':
    view = GameGUI()
    model = Game(view)
    controller = GameController(view, model)
    controller.getGameState()
