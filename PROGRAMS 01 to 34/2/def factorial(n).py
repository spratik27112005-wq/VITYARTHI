import time
import tracemalloc

def prime_factors(n):
    tracemalloc.start()
    start = time.time()
    
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print("Execution time:", end - start, "seconds")
    print("Memory used:", current / 1024, "KB (current),", peak / 1024, "KB (peak)")
    
    return factors

num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))