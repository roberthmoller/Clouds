from time import time

def timed(execution):
    start = time()
    result = execution()
    end = time()
    return (end - start) * 1000, result
