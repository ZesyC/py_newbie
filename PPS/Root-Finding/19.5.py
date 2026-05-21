import numpy as np
    
def my_newton(f, df, y0, tol):
    if np.abs(f(y0)) < tol:
        return y0
    
    if df(y0) == 0:
        raise Exception("Derivative is zero")
    
    y1 = y0 - f(y0)/df(y0)

    if np.abs(f(y1)) < tol:
        return y1
    else:
        return my_newton(f, df, y1, tol)
    
def my_nth_root(x, n, tol):
    if x <= 0 or tol <= 0:
        raise Exception("x and tol must be strictly positive")
    
    if n <= 1:
        raise Exception("n must be an integer strictly greater than 1")
    
    f = lambda y: y**n - x
    df = lambda y: n*y**(n - 1)

    y0 = x

    if np.abs(f(y0)) < tol:
        return y0
    
    y1 = y0 - f(y0)/df(y0)

    if np.abs(f(y1)) < tol:
        return y1
    else:
        return my_newton(f, df, y1, tol)
    
r1 = my_nth_root(2, 2, 0.01)
print(f"r1 = {r1}")
print(f"r1^2 = {r1**2}")

r2 = my_nth_root(27, 3, 0.01)
print(f"r2 = {r2}")
print(f"r2^3 = {r2**3}")
