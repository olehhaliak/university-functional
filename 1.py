import math

# function, root of which I will find
def f(x):
    return x - math.sin(x) - 0.25


def calculate(a, b, eps):
    mid = (a + b) / 2
    if f(mid) == 0 or abs(f(mid)) < eps:
        root = mid
        return root
    elif f(a) * f(mid) < 0:
        return calculate(a, mid, eps)
    else:
        return calculate(mid, b, eps)

print(calculate(-100, 100, 0.0000000001))