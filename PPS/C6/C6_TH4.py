import numpy as np
import math


def taylor_exp_approx(x, order):
    approx = 0.0

    for k in range(order + 1):
        approx += (x**k) / math.factorial(k)

    return approx


def truncation_error_bound_exp(x, order):
    M = np.exp(x) if x > 0 else 1.0

    return (M * abs(x)**(order + 1)) / math.factorial(order + 1)

x = 2.0

for n in range(1, 8):
    print(f"Bậc {n}: {taylor_exp_approx(x, n):.8f}")

error = truncation_error_bound_exp(x, 7)
print(f"Giới hạn sai số cắt cụt bậc 7: {error:.8f}")
