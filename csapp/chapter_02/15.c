/*
 * cs:app 
 * homework 2.61
 * by number29
 * Jan 13, 2021 
 */

#include <stdio.h>


int is_all_one(int x) {
    return !(x + 1);
}


int is_all_zero(int x) {
    return !x;
}


int is_lowest_byte_all_one(int x) {
    unsigned char c = (unsigned char) x;
    unsigned char r = c + 1;
    return !r;
}


int is_highest_byte_all_zero(int x) {
    int shift_val = (sizeof(int) - 1) << 3;
    int xright = x >> shift_val;
    unsigned char c = (unsigned char) xright;
    return !c;
}


int main()
{
    int x1 = -1;
    printf("%d\n", is_all_one(x1));

    int x2 = 0;
    printf("%d\n", is_all_zero(x2));

    int x3 = 0x123456FF;
    int x4 = 0x123456FE;
    printf("%d\n", is_lowest_byte_all_one(x3));
    printf("%d\n", is_lowest_byte_all_one(x4));

    int x5 = 0x12345600;
    int x6 = 0x00345678;
    printf("%d\n", is_highest_byte_all_zero(x5));
    printf("%d\n", is_highest_byte_all_zero(x6));

    return 0;
}
