import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 4) 두 행렬 A와 B의 곱셈
def multiply_matrices(A, B):
    return np.dot(A, B)

print("\n4) 행렬 곱셈:")
print(multiply_matrices(A, B))