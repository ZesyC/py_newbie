import numpy as np

def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
    
    m = (a + b)/ 2

    if np.abs(f(m))< tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)
    else:
        return m
    
f = lambda x: x**2 - 2
r1 = my_bisection(f, 0, 2, 0.1)
print(f"r1 = {r1}")
r01 = my_bisection(f, 0, 2, 0.01)
print(f"r01 = {r01}")

print(f'f(r1) = {f((r1))}')
print(f'f(r01) = {f(r01)}')

try:
    r2 = my_bisection(f, 2, 4, 0.1)
    print(f"r2 = {r2}")
    print(f'f(r2) = {f(r2)}')
except Exception as e:
    print(f"r2 error: {e}")
