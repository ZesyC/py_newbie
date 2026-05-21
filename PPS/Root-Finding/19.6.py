import numpy as np

def my_bisection(F, a, b, tol, max_iter):
    if max_iter == 0:
        return []
    
    m = (a + b)/ 2

    if np.abs(F(m)) < tol:
        return m
    elif np.sign(F(a)) == np.sign(F(m)):
        return my_bisection(F, m, b, tol, max_iter - 1)
    elif np.sign(F(b)) == np.sign(F(m)):
        return my_bisection(F, a, m, tol, max_iter - 1)
    else:
        return m

def my_fixed_point(f, g, tol, max_iter):
    if tol <= 0 or max_iter <= 0:
        raise Exception("tol and max_iter must be strictly positive")
    
    if not isinstance(max_iter, int):
        raise Exception("max_iter must be an integer")
    
    F = lambda x: f(x) - g(x)
    a = 0
    b = 1

    if np.sign(F(a)) == np.sign(F(b)):
        return []
    
    return my_bisection(F, a, b, tol, max_iter)
    
f = lambda x: np.cos(x)
g = lambda x: x

r1 = my_fixed_point(f, g, 0.01, 100)
print(f"r1 = {r1}")
print(f'|f(r1) - g(r1)| = {np.abs(f(r1) - g(r1))}')

r2 = my_fixed_point(f, g, 0.01, 2)
print(f"r2 = {r2}")
