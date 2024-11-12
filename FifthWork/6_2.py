import numpy as np

def LU_decomp(A):
    (n,m) = A.shape
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(0, n):
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(0, i):
                U[i, j] = U[i, j] - L[i, k] * U[k, j]
        L[i, i] = 1
        if i < n-1:
            p = i + 1
            for j in range(0, p):
                L[p, j] = A[p, j]
                for k in range(0, j):
                    L[p, j] = A[p, j] - L[p, k]*U[k, j]
                    L[p, j] = L[p, j]/U[j, j]
    return L, U

def LU_Solver(A, b):
    L, U = LU_decomp(A)
    n = len(L)

    y = np.zeros((n, 1))
    for i in range(0, n):
        y[i] = b[i]
        for k in range(0, i):
            y[i] -= y[k]*L[i, k]
    
    x = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        if i < n-1:
            for k in range(i+1, n):
                x[i] -= x[k]*U[i,k]
        x[i] = x[i]/float(U[i,i])
    return x

A = np.array([[1, 2, 1], [2, 3, 3], [-3, -10, 2]])
b = np.array([[2], [1], [0]])

x = LU_Solver(A,b)
print("x = \n", x)