/*
 * cs:app
 * homework 2.63
 * by number29
 * Jan 14, 2021
 */


#include <stdio.h>
#include <assert.h>


unsigned srl(unsigned x, int k) {
    /* Perform shift arithmetically */
    unsigned xsra = (int) x >> k;
    
    int w = sizeof(int) << 3;
    int mask = (int) -1 << (w - k);
    return xsra & ~mask;
}


unsigned sra(int x, int k) {
    /* Perform shift logically */
    int xsrl = (unsigned) x >> k;

    int w = sizeof(int) << 3;
    int mask = (int) -1 << (w - k);
    int m = 1 << (w - 1);
    mask &= !(x & m) - 1;
    return xsrl | mask;
}


int main(int argc, char *argv[])
{
    unsigned ui = 0x87345678;
    printf("%X\n", srl(ui, 8));
    assert(srl(ui, 8) == (ui >> 8));

    int i = 0x87345678;
    printf("%X\n", sra(i, 8));
    assert(sra(i, 8) == (i >> 8));

    return 0;
}
