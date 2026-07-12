import numpy as np

def qr_decomposition(A):
    A = np.array(A, dtype=float)
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]
        
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
        
    return Q, R

A = [[2, 1, 2],
     [1, 3, 2],
     [2, 4, 1]]

Q, R = qr_decomposition(A)

print("HÀM GRAM-SCHMIDT:")
print("Ma trận Q:\n", Q)
print("\nMa trận R:\n", R)
print("\nXác minh tích Q * R:\n", np.dot(Q, R))