#include <stdio.h>


unsigned int bit_op(unsigned int x, unsigned int y) {
    return ((x << 24) >> 24) | ((y >> 8) << 8);
}


int main()
{
    unsigned int x = 0x89ABCDEF;
    unsigned int y = 0x76543210;
    printf("%X\n", bit_op(x, y));

    return 0;
}
