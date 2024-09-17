import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 3) 두 행렬 A와 B의 뺄셈 (A-B), (B-A)
def subtract_matrix(A, B):
    return A - B, B - A

# 출력
A_minus_B, B_minus_A = subtract_matrix(A, B)
print("3) 행렬 뺄셈 (A-B, B-A):")
print("A - B:\n", A_minus_B)
print("B - A:\n", B_minus_A)
