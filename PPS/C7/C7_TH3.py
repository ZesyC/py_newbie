import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)

x = np.linspace(a, b, n)
y = np.sin(x)

i_simp = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
error = 2 - i_simp

print("Giá trị chính xác: 2.00000000\n")
print(f"Xấp xỉ Simpson: {i_simp:.8f}")
print(f"Sai số: {error:.8f}")
