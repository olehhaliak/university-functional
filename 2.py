import math


def f(x):
    return math.cos(x) / x


def formatted_print(x, y):
    print("|{:5.2f} | {:5.2f}|".format(x, y))


x = 0.5
print("|   X  |   Y  |")
print("|------+------|")

while x <= 11.000001:
    formatted_print(x=x, y=f(x))
    x += 0.3
