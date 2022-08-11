import numpy as np

def check_filled(arr: np.ndarray) -> bool:
    return " " not in arr

def check_win(arr: np.ndarray, symb: str) -> bool:
    for i in range(3):
        if np.all(arr[:, i] == symb) or np.all(arr[i, :] == symb):
            return True
        if np.all(arr.diagonal() == symb) or np.all(np.fliplr(arr).diagonal() == symb):
            return True
    return False