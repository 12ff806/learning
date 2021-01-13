/*
 * cs:app
 * homework 2.59
 * by number29
 * Jan 13, 2021
 */

#include <stdio.h>


unsigned int bit_op(unsigned int x, unsigned int y) {
    return ((x << 24) >> 24) | ((y >> 8) << 8);
}

unsigned bit_op_v2(unsigned x, unsigned y) {
    return (x & 0xFF) | (y & (~0xFF));
}


int main()
{
    unsigned int x = 0x89ABCDEF;
    unsigned int y = 0x76543210;
    printf("%X\n", bit_op(x, y));
    printf("%X\n", bit_op_v2(x, y));

    return 0;
}
