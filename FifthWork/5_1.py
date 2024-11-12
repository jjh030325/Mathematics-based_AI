import numpy as np

A = np.array([[1, -4, 1], [3, 2, 3], [1, 1, 3]])
w1, V1 = np.linalg.eig(A)
print("A의 고윳값 = \n", w1)
print("A의 고유벡터 = \n", V1)

B = np.array([[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]])
w2, V2 = np.linalg.eig(B)
print("\nB의 고윳값 = ", w2)
print("B의 고유벡터 = ", V2)

C = np.array([[2,-1,0,-1], [-1,2,-1,0], [0,-1,2,-1], [-1,0,-1,2]])
w3, V3 = np.linalg.eig(C)
print("\nC의 고윳값 = \n", w3)
print("C의 고유벡터 = \n", V3)