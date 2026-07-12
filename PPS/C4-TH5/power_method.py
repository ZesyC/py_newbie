import numpy as np

def normalize(x):
    factor = np.max(np.abs(x))
    x_normalized = x / factor
    return factor, x_normalized

A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]], dtype=float)

x = np.array([1, 1, 1], dtype=float)

for i in range(8):
    x = np.dot(A, x)
    eigenvalue, x = normalize(x)
    print(f"Iteration {i + 1}:")
    print("Eigenvalue:", eigenvalue)
    print("Eigenvector:", x)

print("\nAfter 8 iterations:")
print("Largest eigenvalue:", eigenvalue)
print("Eigenvector:", x)
