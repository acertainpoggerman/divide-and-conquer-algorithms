from math import ceil, floor, log
import numpy as np


def grid_split(arr: np.ndarray) -> list[np.ndarray]:
    
    arr_1x, arr_2x = np.vsplit(arr, 2)
    arr_11, arr_12 = np.hsplit(arr_1x, 2)
    arr_21, arr_22 = np.hsplit(arr_2x, 2)
    
    return arr_11, arr_12, arr_21, arr_22

def is_power_of(base: int, power: int) -> bool:
    if power == 0: return False
    return ( ceil(log(power, base)) == floor(log(power, base)) )
    
def get_next_power(base: int, value: int) -> int:
    return 2 ** ceil(log(value, base))



def strassen_multiply(A: np.ndarray, B: np.ndarray, n: int) -> np.ndarray:
    
    size_A = len(A), len(A[0])
    size_B = len(B), len(B[0])
    
    size_result = size_A[0], size_B[1]
    
    if size_A[1] != size_B[0]: raise Exception("Row length of A does not equal Column length of B")
    mat_size: int = max(*size_A, *size_B)
    
    if not is_power_of(2, mat_size): mat_size = get_next_power(2, mat_size)
    
    pad_A = (0, mat_size - size_A[0]), (0, mat_size - size_A[1])
    pad_B = (0, mat_size - size_B[0]), (0, mat_size - size_B[1])
    
    A = np.pad(A, pad_A, "constant")
    B = np.pad(B, pad_B, "constant")
    
    if n == 1: return A @ B
    
    A11, A12, A21, A22 = grid_split(A)
    B11, B12, B21, B22 = grid_split(B)
    
    M1 = strassen_multiply(A11 + A22, B11 + B22, n/2)
    M2 = strassen_multiply(A21 + A22, B11, n/2)
    M3 = strassen_multiply(A11, B12 - B22, n/2)
    M4 = strassen_multiply(A22, B21 - B11, n/2)
    M5 = strassen_multiply(A11 + A12, B22, n/2)
    
    M6 = strassen_multiply(A21 - A11, B11 + B12, n/2)
    M7 = strassen_multiply(A12 - A22, B21 + B22, n/2)
    
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    C1X, C2X = np.hstack((C11, C12)), np.hstack((C21, C22))
    return np.vstack((C1X, C2X))[0:size_result[0], 0:size_result[1]]


