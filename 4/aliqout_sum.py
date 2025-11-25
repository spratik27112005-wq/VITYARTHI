import time
import sys

def aliquot_sum(n):
    """Return the sum of all proper divisors of n."""
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s
start_time = time.time()
end_time = time.time()
n = int(input("Enter a number:"))
time_taken = end_time-start_time
print("Aliquot sum of", n, "is:", aliquot_sum(n))
print("time taken:",time_taken,"seconds")
print("memory usaage:",sys.getsizeof(aliquot_sum(n)))
print("thankyou")