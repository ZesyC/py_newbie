import numpy as np

def cholesky_factorization(C):
    L = np.array(C, dtype=float)
    n = L.shape[0]
    
    for k in range(n):
        for i in range(k):
            s = 0.0
            for j in range(i):
                s += L[i, j] * L[k, j]
            L[k, i] = (L[k, i] - s) / L[i, i]
        
        v = 0.0
        for j in range(k):
            v += L[k, j] ** 2
        L[k, k] = np.sqrt(L[k, k] - v)
        
    for i in range(n):
        for j in range(i + 1, n):
            L[i, j] = 0.0
            
    return L

A = [[10, 5, 2],
     [5, 3, 2],
     [2, 2, 3]]

L = cholesky_factorization(A)

print("Ma trận tam giác dưới L")
print(L)

print("\nKiểm chứng: L * L^T")
print(np.dot(L, L.T))

print("\nMa trận tam giác trên U (theo Cholesky decomposition-example.pdf: A = U^T * U):")
print(L.T)
