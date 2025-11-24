
import time
import sys
import resource

def polygonal_number(s, n):
    if s < 3 or n < 1:
        return None
    return n * (n - 1) * (s - 2) // 2 + n


start_time = time.time()
result = polygonal_number(5, 3)  
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print("Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")