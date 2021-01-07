#include <stdio.h>


typedef unsigned char *byte_pointer;


void show_bytes(byte_pointer start, size_t len)
{
    size_t i;
    for (i = 0; i < len; i++)
        printf(" %.2x", start[i]);
    printf("\n");
}


int main()
{
    printf("0 == 0U ? %d\n", 0 == 0U);
    printf("-1 < 0 ? %d\n", -1 < 0);
    printf("-1 < 0U ? %d\n", -1 < 0U);
    printf("-2147483647-1 == 2147483648U ? %d\n", -2147483647-1 == 2147483648U);
    printf("-2147483647-1 < 2147483647 ? %d\n", -2147483647-1 < 2147483647);
    printf("-2147483647-1U < 2147483647 ? %d\n", -2147483647-1U < 2147483647);
    printf("-2147483647-1 < -2147483647 ? %d\n", -2147483647-1 < -2147483647);
    printf("-2147483647-1U < -2147483647 ? %d\n", -2147483647-1U < -2147483647);
    printf("\n");

    short sx = -12345;
    unsigned short usx = sx;
    int x = sx;
    unsigned ux = usx;

    printf("sx = %d:\t", sx);
    show_bytes((byte_pointer) &sx, sizeof(short));
    
    printf("usx = %u:\t", usx);
    show_bytes((byte_pointer) &usx, sizeof(unsigned short));

    printf("x = %d:\t", x);
    show_bytes((byte_pointer) &x, sizeof(int));
    
    printf("ux = %u:\t", ux);
    show_bytes((byte_pointer) &ux, sizeof(unsigned));
    printf("\n");

    short sy = -12345;
    unsigned uy = sy;

    printf("uy = %u:\t", uy);
    show_bytes((byte_pointer) &uy, sizeof(unsigned));

    return 0;
}
