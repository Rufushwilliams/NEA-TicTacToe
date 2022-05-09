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
        self.game = Game()
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
        gameWindow = Toplevel(self.root)
        gameWindow.geometry("300x200")

        tk.Button(gameWindow, text="Dismiss", command=gameWindow.destroy).grid(row=0,column=4)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                txt = tk.StringVar()
                txt.set(" ")
                cmd = lambda r=row,c=col : self.playmove(r,c)
                tk.Button(
                    gameWindow,
                    textvariable=txt,
                    width=6,
                    height=3,
                    command=cmd).grid(row=row, column=col)
                self.buttons[row][col] = txt

        
    
    def playmove(self, row, col):
        self.buttons[row][col].set(self.game.psymbol[self.game.pturn])
        self.game.numplays += 1
        if self.game.pturn == 1:
            self.game.pturn = 2
        else:
            self.game.pturn = 1

            




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
