#include <iostream>
#include <vector>
#include <chrono>
#include <sys/resource.h>

using namespace std;

// Helper function to calculate sum of proper divisors
int sumProperDivisors(int n) {
    int sum = 1;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            sum += i;
            if (i != n / i && i != n / i) { // Check for distinct divisor
                sum += n / i;
            }
        }
    }
    return sum;
}

// Main function to check for amicable numbers
bool amicable(int a, int b) {
    return sumProperDivisors(a) == b && sumProperDivisors(b) == a;
}

// Function to check memory usage using getrusage
long get_mem_usage() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss; // Returns memory usage in KB
}

int main() {
    int a, b;
    cout << "Enter 2 numbers: ";
    cin >> a >> b;

    // Measure start memory and time
    long mem_before = get_mem_usage();
    auto start = chrono::high_resolution_clock::now();

    bool result = amicable(a, b);

    // Measure end memory and time
    auto end = chrono::high_resolution_clock::now();
    long mem_after = get_mem_usage();

    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    cout << (result ? "Amicable Pair\n" : "Not Amicable Pair\n");
    cout << "Execution Time: " << duration.count() << " µs\n";
    cout << "Memory Usage: " << (mem_after - mem_before) << " KB\n";

    return 0;
}
