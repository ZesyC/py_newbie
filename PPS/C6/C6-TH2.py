import math


def taylor_sin_order_4(x):
    return x - x**3 / math.factorial(3)


def taylor_cos_order_4(x):
    return 1 - x**2 / math.factorial(2)


def taylor_sin_cos_order_4(x):
    return x - 2 * x**3 / math.factorial(3)


x = math.pi / 2
actual = math.sin(x) * math.cos(x)

separate_approx = taylor_sin_order_4(x) * taylor_cos_order_4(x)
product_approx = taylor_sin_cos_order_4(x)

print(f"sin(x)cos(x) at x = pi/2: {actual:.8f}")
print(f"Approximate separately, then multiply: {separate_approx:.8f}")
print(f"Error: {abs(actual - separate_approx):.8f}")
print(f"Approximate the product directly: {product_approx:.8f}")
print(f"Error: {abs(actual - product_approx):.8f}")

if abs(actual - separate_approx) < abs(actual - product_approx):
    print("Approximating separately, then multiplying gives the smaller error.")
else:
    print("Approximating the product directly gives the smaller error.")
