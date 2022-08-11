from check import check_filled, check_win, check_occupied
from print_board import print_board
import numpy as np

def game_loop():
    turn = np.random.randint(1, 3)
    symbs = {1: "X", 2: "O"}
    arr = np.array([[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]])
    while True:
        print_board(arr)
        symb = symbs[turn]
        print("\n")
        possible_options = ["0", "1", "2"]
        row = input(f"{symb}'s turn\nSelect row: ")
        col = input("Select col: ")
        if row == "q" or col == "q":
            print("Quitting")
            break

        if row not in possible_options or col not in possible_options:
            choice = input("Wrong input, please enter a number between 0 and 2 (press anything): ")
            if choice == "q":
                print("Quitting")
                break
            continue

        if check_occupied(arr, int(row), int(col)):
            print("\n")
            print("This square is already occupied, try again.")
            continue

        arr[int(row), int(col)] = symb

        if check_win(arr, symb):
            print_board(arr)
            print("\n")
            print(f"{symb} won!")
            input("Press any button to end game: ")
            break
        if check_filled(arr):
            print_board(arr)
            print("\n")
            print("It is a draw")
            input("Press any button to end game: ")
            break

        turn = 2 if turn == 1 else 1

if __name__ == "__main__":
    game_loop()