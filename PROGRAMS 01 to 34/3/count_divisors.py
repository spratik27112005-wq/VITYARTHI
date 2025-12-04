import time
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss 
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
start_time = time.time()
n = int(input("Enter a number to count its divisors: "))
print(f"Number of divisors of {n}: {count_divisors(n)}")
print(f"memory usage :{memory_usage()} bytes")
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.6f} seconds")