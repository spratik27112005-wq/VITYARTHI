import time
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss 
# Input: a positive integer
number = int(input("Enter a number: "))
start_time = time.time()

def mean_of_digits(n) :
    total = 0
    count = 0
    n = number 
    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10
        if count ==0 :
            return 0
        else:
            return total/count
       

print(f"The average of the digits of {number} is {mean_of_digits(number)}")
print(f"memory usage :{memory_usage()} bytes")
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")