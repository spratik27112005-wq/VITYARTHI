def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

number = int(input("Enter a number: "))
print(f"Number of steps until single digit: {multiplicative_persistence(number)}")