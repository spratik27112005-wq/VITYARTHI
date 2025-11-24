import time
import tracemalloc

def mobius(n):
    if n == 1:
        print("1")
    factors = []
    i = 2
    num = n
    while (i * i) <= num:
        count = 0
        while num % i == 0:
            num //= i
            count += 1
        if count > 0:
            if count > 1:
                print("0")
            factors.append(i)
        i += 1
    if num > 1:
        factors.append(num)
    if len(factors) % 2 == 0:
        print("1")
    else:
        print("-1")

# Start measuring time and memory
start_time = time.time()
tracemalloc.start()

# ---- main execution ----
n = int(input("Enter a Number: "))
mobius(n)

# ---- measurement results ----
current, _ = tracemalloc.get_traced_memory()
end_time = time.time()

print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
tracemalloc.stop()
