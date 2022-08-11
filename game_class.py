import numpy as np
from board import board

class game:

    def __init__(self) -> None:
        self.reset()
        self.possible_options = ["0", "1", "2"]

    def reset(self):
        self.board = board()
        self.turn = np.random.randint(1, 3)
        self.symbs = {1: "X", 2: "O"}

    def loop(self) -> None:
        symb = self.symbs[self.turn]
        while True:
            if self.board.check_win(symb):
                self.board.print_board()
                print("\n")
                print(f"{symb} won!")
                input("Press any button to end game: ")
                break
            if self.board.check_filled():
                self.board.print_board()
                print("\n")
                print("It is a draw")
                input("Press any button to end game: ")
                break
            self.board.print_board()
            self.turn = 2 if self.turn == 1 else 1
            symb = self.symbs[self.turn]
            print("\n")
            row = input(f"{symb}'s turn\nSelect row: ")
            col = input("Select col: ")
            if row == "q" or col == "q":
                print("Quitting")
                break

            if row not in self.possible_options or col not in self.possible_options:
                choice = input("Wrong input, please enter a number between 0 and 2 (press anything): ")
                if choice == "q":
                    print("Quitting")
                    break
                continue

            self.board.set_value(int(row), int(col), symb)

if __name__ == "__main__":
    game = game()
    game.loop()