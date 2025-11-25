
import time
import sys
import resource

def partition_function(n):
    if n < 0:
        return 0
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        j = 1
        while True:
            pent = j * (3 * j - 1) // 2
            if pent > i:
                break
            sign = 1 if (j % 2 == 1) else -1
            p[i] += sign * p[i - pent]
            pent_neg = (-j) * (3 * (-j) - 1) // 2
            if pent_neg <= i:
                sign = 1 if (j % 2 == 0) else -1
                p[i] += sign * p[i - pent_neg]
            j += 1
    return p[n]


start_time = time.time()
result = partition_function(10)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")