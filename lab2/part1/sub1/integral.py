from math import sin
from assertions import AssertThat
from numpy import linspace


def f(x: float):
    return abs(sin(x))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


def integral(lower: float, upper: float, N: int):
    AssertThat(lower).isLessThan(upper)
    AssertThat(N).isGreaterThan(0)

    dx = (upper - lower) / N
    stepToX = lambda i: i * dx

    return sum(map(lambda x: dx * f(x), map(stepToX, range(0, N))))


lower = 0
upper = 3.14159

integrals = map(lambda N: integral(lower, upper, N), (10, 100, 1000, 10000, 100000, 1000000))

for intgr in integrals:
    print(intgr)
