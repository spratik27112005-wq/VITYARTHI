import time
import tracemalloc

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

tracemalloc.start()
start_time = time.time()

num = int(input("Enter a non-negative integer: "))
result = factorial(num)

end_time = time.time()
current, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Factorial of", num, "is:", result)
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Memory Usage: {current / 1024:.2f} KB")
