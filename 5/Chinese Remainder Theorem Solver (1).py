
import time
import sys
import resource
from math import gcd

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        return None
    prod = 1
    for m in moduli:
        prod *= m
    result = 0
    for rem, mod in zip(remainders, moduli):
        p = prod // mod
        result += rem * extended_inverse(p, mod) * p
    return result % prod

def extended_inverse(a, m):
    m0, x0, x1 = m, 1, 0
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Test
start_time = time.time()
result = crt([2, 3], [3, 5])
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")