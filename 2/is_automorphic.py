import time
import sys

def is_automorphic(n):
    if n < 0:
        return False
    if n == 0:
        return False  
    
    square = n * n
    temp, digits = n, 0
    while temp > 0:
        digits += 1
        temp //= 10
    
    return square % (10 ** digits) == n

n = int(input("Enter a number:")) 

start_time = time.time()
result = is_automorphic(n)
end_time = time.time()
time_taken = end_time - start_time

print(f"result of {n} is {result}")
print("time taken is", time_taken, "seconds")
print("memory usage of result:", sys.getsizeof(result),"bytes")