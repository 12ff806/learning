#include <stdio.h>


int is_even(int n) {
    if ((n % 2) == 0) {
        return 1;
    }
    return 0;
}


/*
 * Time Complexity: O(logN)
 */
long int pow_cus(long int x, unsigned int n) {
     if (n == 0) {
        return 1;
     }
     if (n == 1) {
        return x;
     }
     if (is_even(n)) {
        return pow_cus(x*x, n/2);
     }
     else {
        return pow_cus(x*x, n/2) * x;
     }
}


int main(int argc, char *argv[]) {
    int x = 2;
    int n = 10;
    int r = pow_cus(x, n);
    printf("pow_cus(%d, %d) = %d\n", x, n, r);
}

