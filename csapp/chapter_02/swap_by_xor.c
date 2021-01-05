#include <stdio.h>


void inplace_swap(int *x, int *y) {
    *y = *x ^ *y;
    printf("y = %d\n", *y);
    *x = *x ^ *y;
    printf("x = %d\n", *x);
    *y = *x ^ *y;
    printf("y = %d\n", *y);
}


void reverse_array(int a[], int cnt) {
    int first, last;
    for (first = 0, last = cnt-1; first < last; first++,last--)
        inplace_swap(&a[first], &a[last]);
}


int main() {
    int a = 1;
    int b = 2;
    inplace_swap(&a, &b);
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    
    int c[] = {1, 2, 3, 4, 5};
    reverse_array(c, 5);
    for (int i = 0; i <= 4; i++)
        printf("c[%d] = %d\n", i, c[i]);
}
