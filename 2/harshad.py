import time
import tracemalloc

def is_harshad(n):
    original = n
    digit_sum = 0
    while n != 0:
        digit = n % 10
        digit_sum += digit
        n = n // 10
    return original % digit_sum == 0

num = 1729

# Start measuring memory and time
tracemalloc.start()
start = time.time()

result = is_harshad(num)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Is Harshad:", result)
print("Runtime: {:.8f} seconds".format(end - start))
print("Peak Memory Usage: {:.8f} MB".format(peak / 10**6))
