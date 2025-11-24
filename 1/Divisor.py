import time
import sys

def divisor_sum(n):
    if not isinstance(n, int) or n < 1:
        print("Input must be a positive integer.")
        return

    steps = 0
    start_time = time.time()
    total_sum = 0
    divisors_list = []

    for i in range(1, n + 1):
        steps += 1
        if n % i == 0:
            total_sum += i
            divisors_list.append(i)

    end_time = time.time()

    memory_used = sys.getsizeof(divisors_list) + sum(sys.getsizeof(d) for d in divisors_list)

    print("Sum of divisors for", n, ":", total_sum)
    print("Steps taken:", steps)
    print("Time taken (seconds):", round(end_time - start_time, 5))
    print("Memory used (approx):", memory_used, "bytes")

divisor_sum(2000)
