#include <stdio.h>


int main()
{
    short int v = -12345;
    unsigned short uv = (unsigned short) v;
    printf("v = %d, uv = %u\n", v, uv);

    unsigned u = 4294967295u;
    int tu = (int) u;
    printf("u = %u, tu = %d\n", u, tu);

    int x = -1;
    unsigned ux = 2147483648;
    printf("x = %u = %d\n", x, x);
    printf("u = %u = %d\n", ux, ux);

    return 0;
}
