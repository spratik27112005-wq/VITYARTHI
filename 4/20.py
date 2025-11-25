import time
import tracemalloc

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:      # if exponent is odd
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent = exponent // 2   # cut exponent in half

    return result

b = int(input("Base: "))
e = int(input("Exponent: "))
m = int(input("Modulus: "))

tracemalloc.start()
start_time = time.time()

answer = mod_exp(b, e, m)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Answer =", answer)
print("Time taken:", (end_time - start_time), "seconds")
print("Memory used:", current, "bytes (current),", peak, "bytes (peak)")
