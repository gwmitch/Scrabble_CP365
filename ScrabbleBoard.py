import numpy as np

class ScrabbleBoard:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype="S1")
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                self.board[row][col] = " "

    def addTile(self, row, col, letter):
        self.board[row][col] = letter

    def getTile(self, row, col):
        return self.board[row][col]

    def isEmpty(self):
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                if self.getTile(row, col) != ' ':
                    return False
        return True

    def __str__(self):
        string_width = 4 * self.board_size + 1
        result = ''
        result += "-" * string_width
        result += '\n'

        for row in range(self.board.shape[0]):
            result += "| "
            for col in range(self.board.shape[1]):
                result += self.board[row][col] + " | "
            result += '\n'

            result += "-" * string_width
            result += '\n'
        return result
