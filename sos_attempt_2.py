import unittest

# Reworking the SOS detection logic with a clearer approach
class Board:
    def __init__(self, size=3, mode="Simple"):
        self.size = size
        self.mode = mode
        self.grid = [["" for _ in range(size)] for _ in range(size)]
        self.turn = 'S'
        self.game_over = False
        self.winner = None

    def make_move(self, row, col, letter):
        if self.grid[row][col] == "" and letter in ['S', 'O'] and not self.game_over:
            self.grid[row][col] = letter
            if self.check_sos(row, col, letter):
                self.winner = self.turn
                self.game_over = True
            else:
                self.turn = 'S' if self.turn == 'O' else 'O'
            return True
        return False

    def check_sos(self, row, col, letter):
        if letter == 'O':  # SOS sequence only possible when 'O' is the center
            if (self.check_direction(row, col, (-1, 0), (1, 0)) or  # Vertical SOS
                self.check_direction(row, col, (0, -1), (0, 1)) or  # Horizontal SOS
                self.check_direction(row, col, (-1, -1), (1, 1)) or  # Diagonal (\) SOS
                self.check_direction(row, col, (-1, 1), (1, -1))):  # Diagonal (/) SOS
                return True
        return False

    def check_direction(self, row, col, dir1, dir2):
        # Ensure valid bounds and check if there's an 'S' in both directions around the 'O'
        try:
            r1, c1 = row + dir1[0], col + dir1[1]
            r2, c2 = row + dir2[0], col + dir2[1]
            if (0 <= r1 < self.size and 0 <= c1 < self.size and
                0 <= r2 < self.size and 0 <= c2 < self.size):
                if self.grid[r1][c1] == 'S' and self.grid[r2][c2] == 'S':
                    return True
        except IndexError:
            pass
        return False

    def is_full(self):
        # Check if the board is full (no empty cells left)
        for row in self.grid:
            if "" in row:
                return False
        return True

    def reset(self):
        # Reset the board for a new game
        self.grid = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.turn = 'S'
        self.game_over = False
        self.winner = None

# Re-running the tests once more to validate the new logic
unittest.main(argv=[''], exit=False)
