/*
 * cs:app
 * homework 2.60
 * by number29
 * Jan 13, 2021
 */

#include <stdio.h>


typedef unsigned char *byte_pointer;


unsigned replace_byte(unsigned x, int i, unsigned char b) {
    byte_pointer start = (byte_pointer) &x;
    int len = sizeof(unsigned);
    if (i >= 0 && i < len) {
        start[i] = b;
        return x;
    }
    else
        return 0;
}


int main()
{
    unsigned x = 0x12345678;
    unsigned r = replace_byte(x, 2, 0xAB);
    printf("%X\n", r);
    
    unsigned r1 = replace_byte(x, 3, 0xAB);
    printf("%X\n", r1);
    
    unsigned r2 = replace_byte(x, 0, 0xAB);
    printf("%X\n", r2);

    return 0;
}
