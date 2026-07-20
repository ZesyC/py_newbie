import numpy as np


def my_int_calc(f, f0, a, b, N, option):
    x = np.linspace(a, b, N)
    h = (b - a) / (N - 1)
    y = f(x)

    if option == "rect":
        return f0 + h * np.sum(y[1:])
    if option == "trap":
        return f0 + (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    if option == "simp":
        return f0 + (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

f = lambda x: x**2

print(my_int_calc(f, 0, 0, 1, 3, "rect"))
print(my_int_calc(f, 0, 0, 1, 3, "trap"))
print(my_int_calc(f, 0, 0, 1, 3, "simp"))
