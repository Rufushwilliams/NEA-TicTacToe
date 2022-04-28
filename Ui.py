from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game = Game()
        while True:
            print(game)
            print(f"It is player {game.pturn}s turn!")
            print("Please enter the row and column you want to play in")
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            game.play(row, col)
            if game.winner != False:
                break
