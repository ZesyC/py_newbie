import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)

x = np.linspace(a, b, n)

i_left = h * np.sum(np.sin(x[:-1]))
error_left = 2 - i_left

i_right = h * np.sum(np.sin(x[1:]))
error_right = 2 - i_right

mid = (x[:-1] + x[1:]) / 2
i_mid = h * np.sum(np.sin(mid))
error_mid = 2 - i_mid

print("Giá trị chính xác: 2.00000000\n")
print(f"Xấp xỉ mút trái: {i_left:.8f} | Sai số: {error_left:.8f}")
print(f"Xấp xỉ mút phải: {i_right:.8f} | Sai số: {error_right:.8f}")
print(f"Xấp xỉ điểm giữa: {i_mid:.8f} | Sai số: {error_mid:.8f}")
