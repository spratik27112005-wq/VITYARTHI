
import time
import sys
import resource
from math import gcd
from random import randint

def pollard(n):
    if n % 2 == 0:
        return 2
    x = randint(1, n - 1)
    y = x
    c = randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    return d


start_time = time.time()
result = pollard(315)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")