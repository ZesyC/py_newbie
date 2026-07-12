import numpy as np

A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]], dtype=float)

Q_builtin, R_builtin = np.linalg.qr(A)

print("HÀM BUILT-IN")
print("Ma trận Q:\n", Q_builtin)
print("\nMa trận R:\n", R_builtin)

print("\nXác minh tính trực giao Q^T * Q:\n", np.round(np.dot(Q_builtin.T, Q_builtin), 4))
print("\nXác minh tích Q * R (Tái tạo ma trận A):\n", np.dot(Q_builtin, R_builtin))