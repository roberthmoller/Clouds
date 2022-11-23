from helpers.assertions import AssertThat
from helpers.timed import timed
from constants import Ns, lower, upper
from math import sin


def f(x: float):
    return abs(sin(x))


def integral(lower: float, upper: float, N: int) -> float:
    AssertThat(lower).isLessThan(upper)
    AssertThat(N).isGreaterThan(0)

    dx = (upper - lower) / N
    stepToX = lambda i: i * dx

    return sum(map(lambda x: dx * f(x), map(stepToX, range(0, N))))


def sample(lower: float, upper: float, over: [int]):
    return map(lambda N: integral(lower, upper, N), over)


if __name__ == '__main__':

    times = []
    for i in range(7):
        executionTime, result = timed(lambda: sample(lower, upper, Ns))
        times.append(executionTime)

    print('\n', ','.join(map("{:.10f}".format, times)))
