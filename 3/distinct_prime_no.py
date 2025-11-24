def count_distinct_prime_factorial(n):
    if n < 2:
        return 0  # 0 and 1 have no prime factors

    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1  # n itself is a prime number

    return count
print(count_distinct_prime_factorial(60))  
  
 
