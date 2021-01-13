/*
 * cs:app
 * homework 2.57
 * by number29
 * Jan 13, 2021
 */

#include <stdio.h>


typedef unsigned char *byte_pointer;


void show_bytes(byte_pointer start, size_t len) {
    size_t i;
    for (i = 0; i < len; i++)
        printf(" %0.2x", start[i]);
    printf("\n");
}


void show_short(short si) {
    show_bytes((byte_pointer) &si, sizeof(short));
}


void show_long(long li) {
    show_bytes((byte_pointer) &li, sizeof(long));
}


void show_float(float f) {
    show_bytes((byte_pointer) &f, sizeof(float));
}

void show_double(double d) {
    show_bytes((byte_pointer) &d, sizeof(double));
}


int main()
{
    short si = 1234;
    show_short(si);
    /*
    printf("%lu\n", sizeof(short));
    */

    long li = 1234;
    show_long(li);

    float f = (float) si;
    show_float(f);

    double d = (double) si;
    show_double(d);

    return 0;
}
