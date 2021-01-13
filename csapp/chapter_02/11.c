/*
 * cs:app
 * homework 2.58
 * by number29
 * Jan 13, 2021
 */

#include <stdio.h>


typedef unsigned char *byte_pointer;


void show_bytes(byte_pointer start, size_t len) {
    size_t i;
    for (i = 0; i < len; i++) {
        printf(" %0.2x", start[i]);
    }
    printf("\n");
}


void show_int(int i) {
    show_bytes((byte_pointer) &i, sizeof(int));
}


int is_little_endian()
{
    /* 0x 00 00 00 01 */
    int i = 1;
    byte_pointer start = (byte_pointer) &i;
    /*
    printf("%d\n", *start);
    return *start;
    */
    return start[0];
}


int main()
{
    int i = 1;
    show_int(i);

    printf("is_little_endian ? %d\n", is_little_endian());
    return 0;
}
