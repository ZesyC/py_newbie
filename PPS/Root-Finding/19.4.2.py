import numpy as np

def my_newton(f, df, x0, tol):
    if np.abs(f(x0)) < tol:
        return x0
    
    if df(x0) == 0:
        raise Exception("Derivative is zero")
    
    x1 = x0 - f(x0)/df(x0)

    if np.abs(f(x1)) < tol:
        return x1
    else:
        return my_newton(f, df, x1, tol)
    
f = lambda x: x**2 - 2
df = lambda x: 2*x

r1 = my_newton(f, df, 1, 0.1)
print(f"r1 = {r1}")
r01 = my_newton(f, df, 1, 0.01)
print(f"r01 = {r01}")

print(f'f(r1) = {f(r1)}')
print(f'f(r01) = {f(r01)}')

try:
    r2 = my_newton(f, df, 1.4, 0.01)
    print(f"r2 = {r2}")
    print(f'f(r2) = {f(r2)}')
except Exception as e:
    print(f"r2 error: {e}")
