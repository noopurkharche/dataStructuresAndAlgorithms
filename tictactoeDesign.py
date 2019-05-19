import os

class Board():
    def __init__(self):
        self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]
    
    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-------------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-------------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        print("-------------")
    
    def update_board(self, cellno, player):
        if self.cells[cellno] == " ":
            self.cells[cellno] = player
    
    def checkWinner(self):
        
        #Check for X win
        if (self.cells[1] == "X" and self.cells[2] == "X" and self.cells[3] == "X") or \
		    (self.cells[4] == "X" and self.cells[5] == "X" and self.cells[6] == "X") or \
		    (self.cells[7] == "X" and self.cells[8] == "X" and self.cells[9] == "X") or \
		    (self.cells[1] == "X" and self.cells[4] == "X" and self.cells[7] == "X") or \
		    (self.cells[2] == "X" and self.cells[5] == "X" and self.cells[8] == "X") or \
		    (self.cells[3] == "X" and self.cells[6] == "X" and self.cells[9] == "X") or \
		    (self.cells[1] == "X" and self.cells[5] == "X" and self.cells[9] == "X") or \
		    (self.cells[3] == "X" and self.cells[5] == "X" and self.cells[7] == "X"):
            os.system("clear")
            self.display()
            print("X wins! Congratulations") 
            exit()
		    
		#Check for O win
        if (self.cells[1] == "O" and self.cells[2] == "O" and self.cells[3] == "O") or \
		    (self.cells[4] == "O" and self.cells[5] == "O" and self.cells[6] == "O") or \
		    (self.cells[7] == "O" and self.cells[8] == "O" and self.cells[9] == "O") or \
		    (self.cells[1] == "O" and self.cells[4] == "O" and self.cells[7] == "O") or \
		    (self.cells[2] == "O" and self.cells[5] == "O" and self.cells[8] == "O") or \
		    (self.cells[3] == "O" and self.cells[6] == "O" and self.cells[9] == "O") or \
		    (self.cells[1] == "O" and self.cells[5] == "O" and self.cells[9] == "O") or \
		    (self.cells[3] == "O" and self.cells[5] == "O" and self.cells[7] == "O"):
            os.system("clear")
            self.display()
            print( "O wins! Congratulations")
            exit()
        
        if self.cells[1] == " " or self.cells[2] == " " or self.cells[3] == " " or self.cells[4] == " " or self.cells[5] == " " or self.cells[6] == " " or self.cells[7] == " " or self.cells[8] == " " or self.cells[9] == " ":
            return " "
        else:
            os.system("clear")
            self.display()
            print("Draw")
            exit()
        
		
board = Board()

while True:
    board.display()
    val = board.checkWinner()
    
    if val == " ":
    
        x_choice = int(input("\n (X) Please choose 1-9.  > "))
        board.update_board(x_choice,"X")
        
        # exit if winner found or draw
        board.checkWinner()
        
        board.display()
    
        o_choice = int(input("\n (O) Please choose 1-9.  > "))
        board.update_board(o_choice,"O")
        
        board.display()
        
        # exit if winner found or draw
        val = board.checkWinner()
    else:
        if val == "X":
            print("Player X wins!!")
            exit()
        else:
            if val == "O":
                print("Player O wins!!")
                exit()
            else:
                if val == "D":
                    print("Game Draw!!")
                    exit()
    
    
