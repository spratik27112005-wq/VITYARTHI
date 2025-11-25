import time
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss 
def is_mersenne_prime(p):
    
    a=2 ** p - 1
    b=0
    c=0
    if p < 2:
        return 0
    for i in range(2,p):
        if p%i==0:
            b=1
            break
        else:
            b=0
        for j in range(2,a):
            if a%i==0:
                c=1
                break
            else:
                c=0
    if b==0 and c==0:
        return True
    else:
        return False
    
start_time = time.time()
p = int(input("Enter a prime number to check if it's a Mersenne prime: "))
if is_mersenne_prime(p):
    print(f"2^{p} - 1 is a Mersenne prime.")
else:
    print(f"2^{p} - 1 is not a Mersenne prime.")
    
print(f"memory usage :{memory_usage()} bytes")
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.6f} seconds")


