import math


def taylor_cos_approx(x, order):
    approx = 0.0

    for k in range(order + 1):
        if k % 2 == 0:
            sign = 1 if k % 4 == 0 else -1
            approx += sign * (x**k) / math.factorial(k)

    return approx


def truncation_error_bound_cos(x, order):
    M = 1.0

    return (M * abs(x)**(order + 1)) / math.factorial(order + 1)

x = 0.2
n = 4

approx = taylor_cos_approx(x, n)
error = truncation_error_bound_cos(x, n)

print(f"Xấp xỉ cos({x}) bậc {n}: {approx:.8f}")
print(f"Giới hạn sai số cắt cụt bậc {n}: {error:.8f}")
