#include <stdio.h>
#include <time.h>

void print_memory_usage() {
    int local_vars = sizeof(int) * 3; // n, sum, i
    printf("Estimated memory usage: %d bytes\n", local_vars);
}

int is_abundant(int n) {
    clock_t start = clock();
    int sum = 0;
    int i;
    for(i = 1; i <= n/2; i++) {
        if(n % i == 0) {
            sum = sum + i;
        }
    }
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Runtime: %.6f seconds\n", time_spent);
    print_memory_usage();
    return (sum > n) ? 1 : 0;
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Is abundant: %s\n", is_abundant(n) ? "true" : "false");
    return 0;
}