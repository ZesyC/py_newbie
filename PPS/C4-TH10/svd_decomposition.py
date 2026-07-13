import numpy as np


def jacobi_eigen_decomposition(matrix, tolerance=1e-10, max_iterations=100):
    A = matrix.copy()
    n = A.shape[0]
    eigenvectors = np.eye(n)

    for _ in range(max_iterations):
        max_value = 0.0
        p, q = 0, 1

        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_value:
                    max_value = abs(A[i, j])
                    p, q = i, j

        if max_value < tolerance:
            break

        if A[p, p] == A[q, q]:
            angle = np.pi / 4
        else:
            angle = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q])

        c = np.cos(angle)
        s = np.sin(angle)

        rotation = np.eye(n)
        rotation[p, p] = c
        rotation[q, q] = c
        rotation[p, q] = -s
        rotation[q, p] = s

        A = rotation.T @ A @ rotation
        eigenvectors = eigenvectors @ rotation

    eigenvalues = np.diag(A)
    return eigenvalues, eigenvectors


def custom_svd(A):
    m, n = A.shape
    eigenvalues, V = jacobi_eigen_decomposition(A.T @ A)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    V = V[:, sorted_indices]

    singular_values = np.sqrt(np.maximum(eigenvalues, 0))
    reduced_size = min(m, n)

    U = np.zeros((m, reduced_size))
    for i in range(reduced_size):
        if singular_values[i] > 1e-10:
            U[:, i] = (A @ V[:, i]) / singular_values[i]

    for i in range(reduced_size):
        norm = np.linalg.norm(U[:, i])
        if norm > 1e-10:
            U[:, i] /= norm

    return U, singular_values[:reduced_size], V.T


A = np.array([[1, 0, 1],
              [-2, 1, 0]], dtype=float)

U, S, Vt = custom_svd(A)

print("Ma trận A:")
print(A)

print("\nCác vector kỳ dị trái (U):")
print(U)

print("\nCác giá trị kỳ dị (Sigma):")
print(S)

print("\nCác vector kỳ dị phải (V):")
print(Vt.T)

print("\nMa trận chuyển vị của các vector phải (V^T):")
print(Vt)

Sigma_matrix = np.zeros((2, 3))
np.fill_diagonal(Sigma_matrix, S)
A_reconstructed = np.dot(U, np.dot(Sigma_matrix, Vt))

print("\nKiểm chứng (U * Sigma * V^T):")
print(np.round(A_reconstructed, 4))
