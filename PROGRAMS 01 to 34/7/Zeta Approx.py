
import time
import sys
import resource

def zeta(s, terms=1000):
    if s <= 1:
        return float('inf')
    total = 0.0
    for k in range(1, terms + 1):
        total += 1 / (k ** s)
    return total


start_time = time.time()
result = zeta(2, 1000)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result:.6f}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")