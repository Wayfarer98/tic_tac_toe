import numpy as np

def print_board(arr: np.ndarray) -> None:
    print(" - - -")
    for i in range(3):
        print(f"|{arr[i,0]}|{arr[i,1]}|{arr[i,2]}|")
        print(" - - -")