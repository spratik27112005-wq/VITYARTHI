import time
import tracemalloc

n=int(input("enter a number: "))

def digital_root(n):
    if n < 0:
        return 0
    return (1 + (n - 1) % 9)

tracemalloc.start()
start_time = time.perf_counter()
result = digital_root(n)
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("digital root:", result)
print("time taken (sec):", end_time - start_time)
print("memory usage (bytes):", current, peak)