import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 6) 행렬 A의 역행렬
def inverse_matrix(A):
    det = np.linalg.det(A)
    if det == 0:
        return "역행렬이 존재하지 않습니다. (행렬식이 0)"
    return np.linalg.inv(A)

print("\n6) 행렬 A의 역행렬:")
print(inverse_matrix(A))
