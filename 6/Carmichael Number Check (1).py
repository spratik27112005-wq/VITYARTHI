
import time
import sys
import resource
from math import gcd

def carmichael(n):
    if n <= 1 or prime(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1 and pow(a, n - 1, n) != 1:
            return False
    return True

def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


start_time = time.time()
result = carmichael(561)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")