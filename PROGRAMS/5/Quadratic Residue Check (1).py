
import time
import sys
import resource

def is_quadratic_residue(a, p):
    if p == 2:
        return True if a % 2 == 0 or a % 2 == 1 else False
    if a % p == 0:
        return True
    return pow(a, (p - 1) // 2, p) == 1

# Test
start_time = time.time()
result = is_quadratic_residue(2, 7)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")