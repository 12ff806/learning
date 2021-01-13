/*
 * cs:app
 * Get most significant byte (p89)
 * by number29
 * Jan 13, 2021
 */

#include <stdio.h>


/* Get most significant byte from x */
int get_msb(int x) {
    /* Shift by w-8 */
    int shift_val = (sizeof(int) - 1) << 3;
    /* Arithmetic shift */
    int xright = x >> shift_val;
    /* Zero all but LSB */
    return xright & 0xFF;
}


int main()
{
    int x = 0x12345678;
    int msb = get_msb(x);
    printf("0x%X\n", msb);

    return 0;
}
