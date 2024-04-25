import tkinter as tk 
import random 
class TicTacToe: 
    def __init__(self, root): 
        self.root = root 
        self.root.title ("TicTacToe")
        self.board = [''or '_' in range(9)]
        self.current_player='X'
        self.buttons{}
        
        for i in range(3):
            for j in range(3):
                button = tk.Button (self.root, text='', width = 10, height = 3, 
                                    command=lambda i=i, j=j:self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)
        self.status_label = tk.Label(self.root, text="X's turn")
        self.status_label.grid(row=3, column=0, columnspan=3)

def click(self, i, j):
    index = 3 * i + j 
    if self.board[index] == '':
        self.board[index] = self.current_player 
        if self.check_winner():
            self.end_game()
        elif ' ' not in self.board: 
            self.end_game(draw=True)
        else: 
            self.current_player = 'X'
            self.status_label. config(text=f"{self.current_player}'s turn")

def check_winner(self):
    lines= [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
            ]
    
