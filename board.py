import numpy as np

class board:

    def __init__(self) -> None:
        self.init_board()

    def init_board(self) -> None:
        self.board = np.full((3, 3), " ")

    def print_board(self) -> None:
        print("-------")
        for i in range(3):
            print(f"|{self.board[i,0]}|{self.board[i,1]}|{self.board[i,2]}|")
            print("-------")

    def check_win(self, symb: str) -> bool:
        for i in range(3):
            if np.all(self.board[:, i] == symb) or np.all(self.board[i, :] == symb):
                return True
            if np.all(self.board.diagonal() == symb) or np.all(np.fliplr(self.board).diagonal() == symb):
                return True
        return False

    def check_filled(self) -> bool:
        return " " not in self.board

    def set_value(self, row: int, col: int, symb: str) -> None:
        self.board[row, col] = symb

    def check_occupied(self, row: int, col: int) -> bool:
        return self.board[row, col] != " "