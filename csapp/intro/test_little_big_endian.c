#include <stdio.h>


typedef unsigned char *byte_pointer;


void show_bytes(byte_pointer start, size_t len) {
    size_t i;
    for (i = 0; i < len; i++)
        printf(" %.2x", start[i]);
    printf("\n");
}


void show_int(int x) {
    show_bytes((byte_pointer) &x, sizeof(int));
}


void show_float(float x) {
    show_bytes((byte_pointer) &x, sizeof(float));
}


void show_pointer(void *x) {
    show_bytes((byte_pointer) &x, sizeof(void *));
}


void test_show_bytes(int val) {
    int ival = val;
    float fval = (float) ival;
    int *pval = &ival;
    show_int(ival);
    show_float(fval);
    show_pointer(pval);
}


int main()
{
    int n1 = 1;
    float n2 = 2.0;
    int n3 = 50;
    int *x1 = &n3;
    show_int(n1);
    show_float(n2);
    show_pointer(x1);
    printf("%lu\n", sizeof(int));
    printf("%lu\n", sizeof(float));
    printf("%lu\n", sizeof(void *));
    printf("%lu\n", sizeof(size_t));
    printf("%lu\n", sizeof(unsigned int));
    printf("%d\n", n1);
    printf("%f\n", n2);
    printf("%d\n", n3);

    test_show_bytes(12345);

    int val = 0x87654321;
    byte_pointer valp = (byte_pointer) &val;
    show_bytes(valp, 1);
    show_bytes(valp, 2);
    show_bytes(valp, 3);

    short m = 12345;
    short n = -m;
    show_bytes((byte_pointer) &m, sizeof(short));
    show_bytes((byte_pointer) &n, sizeof(short));

    short sx = -12345;
    unsigned short usx = sx;
    int x = sx;
    unsigned ux = usx;

    printf("sx = %d:\t", sx);
    show_bytes((byte_pointer) &sx, sizeof(short));

    return 0;
}

