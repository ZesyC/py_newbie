import math
import numpy as np


def my_double_exp(x, n):
    x = np.asarray(x, dtype=float)
    approx = np.zeros_like(x)

    for k in range(n):
        approx += x**(2 * k) / math.factorial(k)

    return approx


x = np.array([-2, -1, 0, 1, 2])

for n in range(1, 6):
    print(f"{n} terms: {my_double_exp(x, n)}")
