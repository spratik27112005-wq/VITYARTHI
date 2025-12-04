import time
import tracemalloc
def count_distinct_prime_factorial(n):
    if n < 2:
        return 0  # 0 and 1 have no prime factors

    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1  # n itself is a prime number

    return count
tracemalloc.start()
start_time = time.time()
print(count_distinct_prime_factorial(60))  
  
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
print("Time taken:", (end_time - start_time), "seconds")
print("Memory used:", current, "bytes (current),", peak, "bytes (peak)")
tracemalloc.stop()