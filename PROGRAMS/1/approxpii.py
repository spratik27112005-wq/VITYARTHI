import time
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss 

def prim_pi(n):

    if n < 2:
        return 0

    count = 0
    
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  
        if is_prime:
            count += 1
    return count

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def prime_pi(x):
 if x<= 1 :
    print("Enter a positive number greater than 1 : ")

 if x > 2 :
    return (x/ln(x))

start_time = time.time()

x =int(input("Enter a number : "))
print(prim_pi(x))
i = float(x)
print("No. of Prime numbers before this number")

print(f"Approximation of prime counting function for this number : ")
app = print(prime_pi(i))
print(f"memory usage :{memory_usage()} bytes")
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.6f} seconds")