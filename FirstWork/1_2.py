import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 2) 두 행렬 A와 B의 덧셈
def add_matrix(A, B):
    return A + B

print("\n2) 행렬 덧셈:")
print(add_matrix(A, B))