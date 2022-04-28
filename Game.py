
class Game:

    def __init__(self):
        self.blank = "-"
        self.pturn = 1
        self.psymbol = {1: "X", 2: "O"}
        self.board = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

    def __repr__(self):
        return self.board

    def play(self,row,col):
        if self.board[row][col] == self.blank:
            self.board[row][col] = self.psymbol[self.pturn]
            if self.pturn == 1:
                self.pturn = 2
            else:
                self.pturn = 1
        else:
            # location has already been played
            pass
    
    @property
    def winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][0] == self.board[row][2]:
                pass

if __name__ == "__main__":
    pass
