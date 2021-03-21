from Presenter.GameViewPresenter import GameViewPresenter
from View import GameGUI as gameGUI
from View.GameGUI import GameGUI

if __name__ == '__main__':
    view = GameGUI()
    presenter = GameViewPresenter(view)
    presenter.getGameState()
