
import time
import sys
import resource
from math import log, sqrt, ceil

def perfectpower(n):
    if n < 1:
        return False
    for b in range(2, int(log(n, 2)) + 1):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False


start_time = time.time()
result = perfectpower(16)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")