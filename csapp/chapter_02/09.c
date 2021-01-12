#include <stdio.h>


int main()
{
    int x1 = 0x7FFFFFFF;
    printf("x1 = %d\n", x1);
    printf("(int)(double) x1 = %d\n", (int)(double) x1);
    printf("x1 == (int)(double) x1 ? %d\n", x1 == (int)(double) x1);
    
    int x2 = 0x80000000;
    printf("x2 = %d\n", x2);
    printf("(int)(double) x2 = %d\n", (int)(double) x2);
    printf("x2 == (int)(double) x2 ? %d\n", x2 == (int)(double) x2);

    int x3 = 0x80000000;
    printf("x3 = %d\n", x3);
    printf("(int)(float) x3 = %d\n", (int)(float) x3);
    printf("x3 == (int)(float) x3 ? %d\n", x3 == (int)(float) x3);

    int x4 = 0x7FFFFFFF;
    printf("x4 = %d\n", x4);
    printf("(int)(float) x4 = %d\n", (int)(float) x4);
    printf("x4 == (int)(float) x4 ? %d\n", x4 == (int)(float) x4);

    double d1 = 1.8e10;
    printf("d1 = %f\n", d1);
    printf("(double)(float) d1 = %f\n", (double)(float) d1);
    printf("d1 == (double)(float) d1 ? %d\n", d1 == (double)(float) d1);

    float f1 = 1e30;
    printf("f1 = %f\n", f1);
    printf("(float)(double) f1 = %f\n", (float)(double) f1);
    printf("f1 == (float)(double) f1 ? %d\n", f1 == (float)(double) f1);

    float f2 = 1e30;
    printf("f2 = %f\n", f2);
    printf("-(-f2) = %f\n", -(-f2));
    printf("f2 == -(-f2) ? %d\n", f2 == -(-f2));

    printf("1.0/2 = %f\n", 1.0/2);
    printf("1/2.0 = %f\n", 1/2.0);

    double d2 = 1.0e155;
    printf("d2*d2 = %f\n", d2*d2);

    float f3 = 1.0e20;
    double d3 = 1.0;
    printf("f3=%f\n", f3);
    printf("d3=%f\n", d3);
    printf("(f3+d3)-f3 == %f\n", (f3+d3)-f3);
    printf("(f3+d3)-f3 == d3 ? %d\n", (f3+d3)-f3 == d3);

    return 0;
}
