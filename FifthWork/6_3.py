import numpy as np

A = np.array([[6, 4], [0, 0], [4, 0]])
print("A = \n", A)
print("\n")

U, Sig, VT = np.linalg.svd(A)
print("U= \n", U)
print("\n")

m, n = A.shape
Sigma = np.zeros((m, n))
k = np.size(Sig)
Sigma[:k, :k] = np.diag(Sig)
print("Sigma = \n", Sigma)
print("\n")
print("V^T = \n", VT)
print("\n")

B = np.array([[1, 1, -1], [0, 1, 1]])
print("B = \n", B)
print("\n")

U, Sig, VT = np.linalg.svd(B)
print("U= \n", U)
print("\n")

m, n = B.shape
Sigma = np.zeros((m, n))
k = np.size(Sig)
Sigma[:k, :k] = np.diag(Sig)
print("Sigma = \n", Sigma)
print("\n")
print("V^T = \n", VT)
print("\n")