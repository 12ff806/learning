#include <stdio.h>


int uadd_ok(unsigned x, unsigned y);


int main()
{
    unsigned x = 2147483648;
    unsigned y = 2147483648;
    printf("%d\n", uadd_ok(x, y));
    return 0;
}

int uadd_ok(unsigned x, unsigned y) {
    unsigned sum = x + y;
    return sum >= x;
}
