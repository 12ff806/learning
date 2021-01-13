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
    else {
        printf("error: invalid i\n");
        return 0;
    }
}


unsigned replace_byte_v2(unsigned x, int i, unsigned char b) {
    if (i < 0 || i >= sizeof(unsigned)) {
        printf("error: invalid i\n");
        return 0;
    }

    return (x & ~(((unsigned) 0xFF) << (i << 3))) | (((unsigned) b) << (i << 3));
}


int main()
{
    unsigned x = 0x12345678;
    
    unsigned r = replace_byte(x, 0, 0xAB);
    printf("%X\n", r);
    unsigned r1 = replace_byte(x, 1, 0xAB);
    printf("%X\n", r1);
    unsigned r2 = replace_byte(x, 2, 0xAB);
    printf("%X\n", r2);
    unsigned r3 = replace_byte(x, 3, 0xAB);
    printf("%X\n", r3);
    unsigned r4 = replace_byte(x, 4, 0xAB);
    printf("%X\n", r4);
    

    unsigned r5 = replace_byte_v2(x, 0, 0xAB);
    printf("%X\n", r5);
    unsigned r6 = replace_byte_v2(x, 1, 0xAB);
    printf("%X\n", r6);
    unsigned r7 = replace_byte_v2(x, 2, 0xAB);
    printf("%X\n", r7);
    unsigned r8 = replace_byte_v2(x, 3, 0xAB);
    printf("%X\n", r8);
    unsigned r9 = replace_byte_v2(x, 4, 0xAB);
    printf("%X\n", r9);

    return 0;
}
