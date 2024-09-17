import numpy as np

# 행렬 A와 B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 1) 두 행렬 A와 B의 크기 (행/열) 출력
def print_matrix_shape(A, B):
    print("행렬 A 크기(행/열):", A.shape)
    print("행렬 B 크기(행/열):", B.shape)

# 실행
print("1) 행렬 크기:")
print_matrix_shape(A, B)