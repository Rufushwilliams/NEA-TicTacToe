import numpy as np
import itertools


class Game:

    def __init__(self):
        self.numplays = 0
        self.blank = "-"
        self.pturn = 1
        self.psymbol = {1: "X", 2: "O"}
        self.board = np.array([["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]])

    def __repr__(self):
        return self.board
    
    def posplay(self, row, col):
        if self.board[row][col] == self.blank:
            return True
        else:
            return False

    def play(self,row,col):
        self.board[row][col] = self.psymbol[self.pturn]
        self.numplays += 1
        if self.pturn == 1:
            self.pturn = 2
        else:
            self.pturn = 1


    def get_winner(self):
        for line in itertools.chain(
                        self.board,
                        self.board.transpose(),
                        (self.board.diagonal(),
                        self.board.transpose().diagonal())):
            if (line==self.psymbol[1]).all():
                return 1
            elif (line==self.psymbol[2]).all():
                return 2
        return 0

if __name__ == "__main__":
    pass
