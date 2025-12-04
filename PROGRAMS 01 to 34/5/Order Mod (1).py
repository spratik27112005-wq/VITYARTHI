
import time
import sys
import resource

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None
    k = 1
    pow_a = a % n
    while pow_a != 1:
        pow_a = (pow_a * a) % n
        k += 1
        if k > n:  # Cycle detection
            return None
    return k

from math import gcd

start_time = time.time()
result = order_mod(2, 7)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")