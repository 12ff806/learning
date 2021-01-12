#include <stdio.h>


int div16(int x) {
    /* Compute bias to be either 0 (x >= 0) or 15 (x < 0) */
    int bias = (x >> 31) & 0xF;
    return (x + bias) >> 4;
}


int main()
{
    int x = 32;
    int y = -31;
    printf("%d / 16 = %d\n", x, div16(x));
    printf("%d / 16 = %d\n", y, div16(y));
    printf("-31 / 16 = %d\n", -31/16);
    return 0;
}
