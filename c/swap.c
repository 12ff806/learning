#include <stdio.h>


void swap(int *, int *);


int main(int argc, char *argv[])
{
    int x = 1;
    int y = 2;
    swap(&x, &y);
    printf("x = %d, y = %d\n", x, y);
    return 0;
}


void swap(int *px, int *py)
{
    int temp;
    temp = *px;
    *px = *py;
    *py = temp;
}
