import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize variables
        self.current_player = 'X'
        self.board = [[' ']*3 for _ in range(3)]

        # Create buttons
        self.buttons = [[tk.Button(root, text=' ', font=('normal', 20), width=6, height=3,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                         for col in range(3)] for row in range(3)]

        # Place buttons on the grid
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            # Update the board and button text for human move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner or draw after human move
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch player for computer move
                self.current_player = 'o'
                # Call computer move function
                self.computer_move()
                # Switch player back to human
                self.current_player = 'X'

    def computer_move(self):
        # Implement a basic random move for the computer
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            # Choose a random empty cell
            row, col = random.choice(empty_cells)
            # Update the board and button text for computer move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner or draw after computer move
            if self.check_winner():
                messagebox.showinfo("Game Over", f"computer {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False  # There is an empty space, game is not a draw
        return True  # All spaces are filled, game is a draw

    def reset_game(self):
        # Reset the game state
        self.current_player = 'X'
        self.board = [[' ']*3 for _ in range(3)]

        # Reset button texts
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

