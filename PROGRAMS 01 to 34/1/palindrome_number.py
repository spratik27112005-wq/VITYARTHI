import time
import tracemalloc

def is_palindrome(number):
    # Handle negative numbers (not typically palindromes)
    if number < 0:
        return False
    
    # Convert number to string for comparison
    num_str = str(number)
    # Compare string with its reverse
    return num_str == num_str[::-1]

def main():
    # Test cases
    test_numbers = [121, 12321, 12345, 1000001, -121]
    
    # Start tracking memory
    tracemalloc.start()
    
    for num in test_numbers:
        # Measure time
        start_time = time.time()
        result = is_palindrome(num)
        end_time = time.time()
        
        # Get memory usage
        current, peak = tracemalloc.get_traced_memory()
        
        print(f"Number: {num}")
        print(f"Is Palindrome: {result}")
        print(f"Time taken: {(end_time - start_time)*1000000:.2f} microseconds")
        print(f"Current memory usage: {current / 1024:.2f} KB")
        print(f"Peak memory usage: {peak / 1024:.2f} KB")
        print("-" * 30)
    
    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    main()