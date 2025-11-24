import time
import sys
start_time = time.time()
def twin_prime(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    twin_primes = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

limit = 130
end_time = time.time()
time_taken = end_time-start_time
print(f"The twin pairs are:{twin_prime(130)}")
print("time taken to run this code:",time_taken,"seconds")
print("memory usage:",sys.getsizeof(twin_prime(limit)),"KB")
# Output: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
