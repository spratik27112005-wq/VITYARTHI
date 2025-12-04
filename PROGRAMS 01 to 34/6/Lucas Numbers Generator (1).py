
import time
import sys
import resource

def lucas(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    s = [2, 1]
    for i in range(2, n + 1):
        s.append(s[-1] + s[-2])
    return s[:n]


start_time = time.time()
result = lucas(10)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")