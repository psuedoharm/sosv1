import tkinter as tk
from tkinter import simpledialog

# Game logic class for handling board and placements
class Board:
    def __init__(self, size=3, mode="Simple"):
        self.size = size
        self.mode = mode
        self.grid = [["" for _ in range(size)] for _ in range(size)]

    def make_move(self, row, col, letter):
        if self.grid[row][col] == "":
            self.grid[row][col] = letter
            return True
        return False


# GUI class for user interface
class SOSGameUI:
    def __init__(self, root, board_size=3, game_mode="Simple"):
        self.root = root
        self.board = Board(size=board_size, mode=game_mode)
        self.current_turn = 'S'
        self.buttons = []
        self.create_board()

    def create_board(self):
        # Create a grid of buttons for the game board
        for row in range(self.board.size):
            row_buttons = []
            for col in range(self.board.size):
                button = tk.Button(self.root, text="", width=10, height=4, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        self.update_status_label()

    def make_move(self, row, col):
        if self.board.make_move(row, col, self.current_turn):
            # Update the button text to show the player's move
            self.buttons[row][col].config(text=self.current_turn)
            # Switch turn between 'S' and 'O'
            self.current_turn = 'S' if self.current_turn == 'O' else 'O'
            self.update_status_label()
        else:
            print("Invalid move. Space is occupied by " + self.current_turn + ". Try again.") # Need to change this to display correct current occupied spot.

    def update_status_label(self):
        # Update the status label to show whose turn it is
        if hasattr(self, 'status_label'):
            self.status_label.config(text=f"Player {self.current_turn}'s turn")
        else:
            self.status_label = tk.Label(self.root, text=f"Player {self.current_turn}'s turn")
            self.status_label.grid(row=self.board.size + 1, column=0, columnspan=self.board.size)

def start_game():
    root = tk.Tk()
    root.title("SOS Game")

    # Ask the user for the board size and game mode
    board_size = simpledialog.askinteger("Board Size", "Enter board size (e.g., 3 for 3x3):", minvalue=3, maxvalue=10)
    game_mode = simpledialog.askstring("Game Mode", "Enter game mode (Simple/General):", initialvalue="Simple")

    # Start the SOS game with the chosen board size and mode
    app = SOSGameUI(root, board_size=board_size, game_mode=game_mode)
    root.mainloop()

if __name__ == "__main__":
    start_game()
