import math
import numpy as np


def my_cosh_approximator(x, n):
    x = np.asarray(x, dtype=float)
    approx = np.zeros_like(x)

    for k in range(n + 1):
        if k % 2 == 0:
            approx += x**k / math.factorial(k)

    return approx


x = np.array([-2, -1, 0, 1, 2])

print(my_cosh_approximator(x, 0))
print(my_cosh_approximator(x, 1))
print(my_cosh_approximator(x, 2))
print(my_cosh_approximator(x, 3))
print(my_cosh_approximator(x, 10))
