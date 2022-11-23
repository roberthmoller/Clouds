import logging
from typing import List

import azure.functions as func
from math import sin

Ns: List[int] = (10, 100, 100, 1000, 10000, 100000, 1000000)
# lower: float = 0
# upper: float = 3.14159


def f(x: float):
    return abs(sin(x))


def integral(lower: float, upper: float, N: int) -> float:
    dx = (upper - lower) / N
    def stepToX(i): return i * dx

    return sum(map(lambda x: dx * f(x), map(stepToX, range(0, N))))


def sample(lower: float, upper: float, over: List[int]):
    return map(lambda N: integral(lower, upper, N), over)


def main(req: func.HttpRequest) -> func.HttpResponse:
    lower = float(req.route_params.get('lower'))
    upper = float(req.route_params.get('upper'))
    logging.info(f'GET /api/integral/{lower}/{upper}')

    integrals = ','.join(
        map("{:10.10f}".format, sample(lower, upper, Ns)))

    return func.HttpResponse(integrals)
