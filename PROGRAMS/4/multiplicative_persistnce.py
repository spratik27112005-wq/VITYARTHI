import time
import tracemalloc
def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

tracemalloc.start()
start_time = time.time()

number = int(input("Enter a number: "))
print(f"Number of steps until single digit: {multiplicative_persistence(number)}")
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
print("Time taken:", (end_time - start_time), "seconds")
print("Memory used:", current, "bytes (current),", peak, "bytes (peak)")