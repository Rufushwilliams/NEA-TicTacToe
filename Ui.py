from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import Toplevel
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = tk.Tk()
        root.geometry("300x200")
        root.resizable(True, True)
        root.title("Tic Tac Toe")
        frame = tk.Frame(root)
        frame.pack()
        self.root = root

        tk.Button(
            frame,
            text="Play",
            command= self.playgame).pack(fill=tk.X)
        tk.Button(
            frame,
            text="Help",
            command= self.gamehelp).pack(fill=tk.X)
        tk.Button(
            frame,
            text="Quit",
            command= root.quit).pack(fill=tk.X)

    def gamehelp(self):
        pass
    
    def playgame(self):
        self.game = Game()
        gameWindow = Toplevel(self.root)
        frame = tk.Frame(gameWindow)
        frame.grid(row=0, col=0)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        b = tk.StringVar()
        b.set(self.game.at(row+1,col+1))

        for row in range(3):
            for col in range(3):
                cmd = lambda r=row,c=col : self.playmove(r,c)
                tk.Button(
                    frame,
                    textvariable=b,
                    command=cmd).grid(row=row, col=col)
                self.buttons[row][col] = b

        tk.Button(gameWindow, text="Dismiss", command=gameWindow.destroy).grid(row=1,column=0)
    
    def playmove(self, row, col):
        pass

            




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
