import math
import time
import os
import psutil
import matplotlib.pyplot as plt

def memoryusage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def primefactorspowers(n):
    f = []
    p = 2
    while p * p <= n:
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        if power > 0:
            f.append((p, power))
        p += 1
    if n > 1:
        f.append((n, 1))
    return f
def carmichaelprimepower(p, k):
    if p == 2 and k >= 3:
        return 2 ** (k - 2)
    return (p - 1) * (p ** (k - 1))

def carmichael(n):
    if n == 1:
        return 1
    factors = primefactorspowers(n)
    v = []
    for p, k in factors:
        v.append(carmichaelprimepower(p, k))
    result = v[0]
    for value in v[1:]:
        result = lcm(result, value)
    return result


start_time = time.time()
n = int(input("Enter a positive integer n: "))
print("Carmichael lambda(n) =", carmichael(n))
print(f"memory usage :{memoryusage()} bytes")
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.6f} seconds")

x = list(range(1,51))
lam_values = [carmichael(n) for n in x]

plt.figure(figsize=(10, 6))
plt.plot(x, lam_values, marker='o', color='steelblue', label='λ(n)')
plt.title('Carmichael Function λ(n) for n = 1 to 50')
plt.xlabel('n')
plt.ylabel('λ(n)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('carmichael_lambda_plot.png')
plt.show()

