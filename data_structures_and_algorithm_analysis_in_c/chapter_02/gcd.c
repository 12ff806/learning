#include <stdio.h>


/*
 * Time Complexity: O(logN)
 */
unsigned int gcd(unsigned int m, unsigned int n) {
    unsigned int rem;

    while (n > 0) {
        rem = m % n;
        m = n;
        n = rem;
    }
    return m;
}


int main(int argc, char *argv[]) {
    int m = 15;
    int n = 50;
    int g = gcd(m, n);
    printf("gcd: %d\n", g);
}

