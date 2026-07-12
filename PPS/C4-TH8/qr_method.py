import numpy as np


A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]], dtype=float)

Ak = A.copy()
iterations_to_print = {1, 2, 5, 7, 10}

print("QR method:")
for i in range(10):
    Q, R = np.linalg.qr(Ak)
    Ak = R @ Q

    if i + 1 in iterations_to_print:
        print(f"\nIteration {i + 1}:")
        print(Ak)
        print("Eigenvalues:", np.diag(Ak))

print("\nAfter 10 iterations:")
print("Eigenvalues from QR method:", np.diag(Ak))

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nUsing Python built-in function:")
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
