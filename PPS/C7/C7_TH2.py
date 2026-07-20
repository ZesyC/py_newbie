import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)

x = np.linspace(a, b, n)
y = np.sin(x)

i_trap = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
error = 2 - i_trap

print("Giá trị chính xác: 2.00000000\n")
print(f"Xấp xỉ hình thang: {i_trap:.8f}")
print(f"Sai số: {error:.8f}")
