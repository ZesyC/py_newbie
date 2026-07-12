import numpy as np


def normalize(x):
    factor = np.max(np.abs(x))
    x_normalized = x / factor
    return factor, x_normalized


def rayleigh_quotient(A, x):
    return np.dot(x, A @ x) / np.dot(x, x)


A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]], dtype=float)

x = np.array([1, 1, 1], dtype=float)

max_iterations = 1000
tolerance = 1e-8
previous_eigenvalue = None

for i in range(max_iterations):
    y = np.linalg.solve(A, x)
    _, x = normalize(y)
    eigenvalue = rayleigh_quotient(A, x)

    if i < 8:
        print(f"Iteration {i + 1}:")
        print("Eigenvalue:", eigenvalue)
        print("Eigenvector:", x)

    if previous_eigenvalue is not None:
        error = abs(eigenvalue - previous_eigenvalue)
        if error < tolerance:
            break

    previous_eigenvalue = eigenvalue

print(f"\nAfter {i + 1} iterations:")
print("Smallest eigenvalue:", eigenvalue)
print("Eigenvector:", x)
