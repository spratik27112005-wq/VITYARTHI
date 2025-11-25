#include <stdio.h>
#include <time.h> // For clock()

// Function to calculate memory usage of variables
void print_memory_usage() {
    // Memory for variables in main()
    int main_vars = sizeof(int) * 2; // a, p
    // Memory for variables in mod_pow()
    int mod_pow_vars = sizeof(int) * 3; // base, exp, mod
    int legendre_vars = sizeof(int) * 2; // a, p
    int local_vars = sizeof(int) * 2; // result, b in mod_pow; ls in legendre_symbol
    int total_memory = main_vars + mod_pow_vars + legendre_vars + local_vars;

    printf("Estimated memory usage:\n");
    printf("  main() variables: %d bytes (a, p)\n", main_vars);
    printf("  mod_pow() variables: %d bytes (base, exp, mod)\n", mod_pow_vars);
    printf("  legendre_symbol() variables: %d bytes (a, p)\n", legendre_vars);
    printf("  Local variables: %d bytes (result, b, ls)\n", local_vars);
    printf("  Total estimated stack memory: %d bytes\n", total_memory);
}

int mod_pow(int base, int exp, int mod) {
    int result = 1;
    int b = base % mod;
    while (exp > 0) {
        if (exp & 1)
            result = (result * b) % mod;
        b = (b * b) % mod;
        exp >>= 1;
    }
    return result;
}

int legendre_symbol(int a, int p) {
    if (a % p == 0)
        return 0;
    int ls = mod_pow(a, (p - 1) / 2, p);
    if (ls == 1)
        return 1;
    else if (ls == p - 1)
        return -1;
    else
        return 0; // for completeness, but shouldn't happen if p is prime
}

int main() {
    clock_t start = clock(); // Start timing

    int a, p;
    printf("Enter a (integer): ");
    scanf("%d", &a);
    printf("Enter p (odd prime): ");
    scanf("%d", &p);

    if (p <= 2 || p % 2 == 0) {
        printf("p must be an odd prime number.\n");
        return 1;
    }

    int result = legendre_symbol(a, p);
    printf("Legendre symbol (%d/%d) = %d\n", a, p, result);

    // Calculate and print runtime
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Execution time: %.6f seconds\n", time_spent);

    // Print memory usage
    print_memory_usage();

    return 0;
}