import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = {}

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=' ', width=10, height=3,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

        self.status_label = tk.Label(self.root, text="X's turn")
        self.status_label.grid(row=3, column=0, columnspan=3)

    def on_click(self, i, j):
        index = 3 * i + j
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[(i, j)].config(text=self.current_player)
            if self.check_winner():
                self.end_game()
            elif ' ' not in self.board:
                self.end_game(draw=True)
            else:
                self.current_player = 'O' 
                self.status_label.config(text="Computer's turn")
                self.computer_move()

    def computer_move(self):
        empty_indices = [i for i, val in enumerate(self.board) if val == ' ']
        index = random.choice(empty_indices)
        i, j = divmod(index, 3)
        self.board[index] = 'O'
        self.buttons[(i, j)].config(text='O')
        if self.check_winner():
            self.end_game()
        elif ' ' not in self.board:
            self.end_game(draw=True)
        else:
            self.current_player = 'X'
            self.status_label.config(text="X's turn")

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def end_game(self, draw=False):
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)
        if draw:
            self.status_label.config(text="It's a draw!")
        else:
            winner = 'Player' if self.current_player == 'O' else 'Computer'
            self.status_label.config(text=f"{winner} wins!")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
