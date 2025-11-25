import time
import tracemalloc   

def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_phi(n):
    if n <= 0:
        return 0
    count = 0
    for k in range(1, n + 1):
        if my_gcd(n, k) == 1:
            count += 1
    return count

num = int(input("Enter a positive integer: "))

tracemalloc.start()
start_time = time.perf_counter()

result = euler_phi(num)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()  
tracemalloc.stop()


print("Euler's Totient Function value is:", result)
print("Time taken (seconds):", end_time - start_time)
print("Current memory usage (bytes):", current)
print("Peak memory usage (bytes):", peak)
