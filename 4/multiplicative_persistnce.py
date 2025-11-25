num=int(input("Enter a number to check if it is highly composite: "))
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def is_highly_composite(n):
    n_div = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= n_div:
            return False
    return True


if is_highly_composite(num):
    print(f"{num} is a highly composite number.")
else:
    print(f"{num} is NOT a highly composite number.")

