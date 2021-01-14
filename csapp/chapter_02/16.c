/*
 * cs:app
 * int_shifts_are_arithmetic/ homework 2.62
 * by number29
 * Jan 13, 2021
 */


#include <stdio.h>
#include <assert.h>


int int_shifts_are_arithmetic() {
    return !(-1 ^ (-1 >> 1));
    /*
    return !(~((~0)>>1));
    */
}


int main(int argc, char *argv[]) 
{
    assert(int_shifts_are_arithmetic());
    printf("%d\n", int_shifts_are_arithmetic());

    return 0;
}

