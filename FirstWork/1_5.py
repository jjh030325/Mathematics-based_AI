import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 5) 행렬 A의 행렬식
def determinant_matrix(A):
    return np.linalg.det(A)

print("\n5) 행렬 A의 행렬식:")
print(determinant_matrix(A))