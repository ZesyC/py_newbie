import numpy as np

A = np.array([[5, 4, 1],
              [5, 5, 0],
              [0, 0, 5],
              [1, 0, 4]], dtype=float)

U, S, Vt = np.linalg.svd(A)

print("Các giá trị đơn lẻ (Sigma):", S)

u1 = U[:, 0:1]
v1 = Vt[0:1, :].T
A1 = np.dot(u1, v1.T)

u2 = U[:, 1:2]
v2 = Vt[1:2, :].T
A2 = np.dot(u2, v2.T)

A_hat_2 = S[0] * A1 + S[1] * A2

print("\nMa trận xấp xỉ hạng 1 thứ nhất (A1):")
print(np.round(A1, 4))

print("\nMa trận xấp xỉ hạng 1 thứ hai (A2):")
print(np.round(A2, 4))

print("\nMa trận kết hợp xấp xỉ hạng 2 (A_hat_2):")
print(np.round(A_hat_2, 4))