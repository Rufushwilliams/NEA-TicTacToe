from abc import ABC, abstractmethod
import tkinter as tk
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = tk.Tk()
        root.title("Tic Tac Toe")
        frame = tk.Frame(root)
        frame.pack()
        self.root = root

        tk.Button(
            frame,
            text='Show Help',
            command= self.gamehelp).pack(fill="x")

        tk.Button(
            frame,
            text='Play Game',
            command= self.playgame).pack(fill="x")

        tk.Button(
            frame,
            text='Quit',
            command=root.quit).pack(fill="x")

    def gamehelp(self):
        pass
    
    def playgame(self):
        game = Game()

    def run(self):
        self.root.mainloop()

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game = Game()
        while True:
            print(game)
            print(f"It is player {game.pturn}s turn!")
            print("Please enter the row and column you want to play in")
            while True:
                while True:
                    row = int(input("Enter the row: "))
                    if 1 <= row and row <= 3:
                        break
                row -= 1
                while True:
                    col = int(input("Enter the column: "))
                    if 1 <= col and col <= 3:
                        break
                col -= 1
                if game.posplay(row, col):
                    break
                else:
                    print("That position has already been played!")
            game.play(row, col)
            winner = game.get_winner()
            if winner != 0:
                break
            elif game.numplays == 9:
                break
        print(game)
        if winner != 0:
            print(f"Congratulations! Player {winner} is the winner!")
        else:   
            print("Sorry, your game ended in a draw.")
