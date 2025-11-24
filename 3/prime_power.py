import time
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss
def is_prime_power(n):
    if n < 2:
        return False
    for p in range(2, int(n**0.5)+1):
        # check if p is prime
        is_prime = True
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        # try different k values
        k = 1
        value = p
        while value < n:
            value *= p
            k += 1
        if value == n:
            return True
    return False
start_time = time.time()
n = int(input("Enter a number to check if it's a prime power: "))
if is_prime_power(n):       
    print(f"{n} is a prime power.")
else:                                       
    print(f"{n} is not a prime power.") 
    
print(f"memory usage :{memory_usage()} bytes")
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.6f} seconds")