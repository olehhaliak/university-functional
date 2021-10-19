import math


def f(x):
    return math.cos(x) / x

x = 0.5
print("|   X  |   Y  |")
print("|------+------|")
while x <= 11.000001:
    print("|{:5.2f} | {:5.2f}|".format(x, f(x)))
    x += 0.3
