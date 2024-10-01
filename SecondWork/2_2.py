import numpy as np

A = np.array([[1,0,0,1],[0,1,2,0],[0,2,1,0],[1,0,0,5]])
A_inv = np.linalg.matrix_power(A, -1)
print("(a) Inverse matrix of A = \n", A_inv)
print("\n")

B = np.array([[2,3],[3,4]])
B_inv = np.linalg.matrix_power(B, -1)
print("(b) Inverse matrix of B = \n", B_inv)
print("\n")

C = np.array([[9,-4,6],[5,-3,6],[-3,1,-2]])
C_inv = np.linalg.matrix_power(C, -1)
print("(c) Inverse matrix of C = \n", C_inv)