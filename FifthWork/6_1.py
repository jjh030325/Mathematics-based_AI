import numpy as np

def LU_decomp(A):
    (n, m) = A.shape
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(0, n):
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(0, i):
                U[i, j] = U[i, j] - L[i, k]*U[k, j]
        L[i, i] = 1
        if i < n-1:
            p = i + 1
            for j in range(0, p):
                L[p, j] = A[p, j]
                for k in range(0, j):
                    L[p, j] = L[p, j] - L[p, k]*U[k, j]
                    L[p, j] = L[p, j]/U[j, j]
    return L, U

A = np.array([[1, 2, 1], [2, 3, 3], [-3, -10, 2]])

L, U = LU_decomp(A)

print("A = \n", A)
print("\n")
print("L = \n", L)
print("\n")
print("U = \n", U)
print("\n")