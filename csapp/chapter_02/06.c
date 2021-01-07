#include <stdio.h>


// 检测无符号数加法中的溢出 没有产生溢出返回1
int uadd_ok(unsigned x, unsigned y);
// 检测补码加法中的溢出 没有产生溢出返回1
int tadd_ok(int x, int y);
// 检测补码减法中的溢出 没有产生溢出返回1
int tsub_ok(int x, int y);
// 检测补码乘法中的溢出 没有产生溢出返回1
int tmult_ok(int x, int y);
int tmult_ok_v2(int x, int y);


int main()
{
    unsigned x = 2147483648;
    unsigned y = 2147483648;
    printf("x+y=%d, %d\n", x+y, uadd_ok(x, y));

    int m = 2147483647;
    int n = 1;
    printf("m+n=%d, %d\n", m+n, tadd_ok(m, n));

    int j = -1;
    int k = -2147483648;
    printf("j-k=%d, %d\n", j-k, tsub_ok(j, k));

    int o = 2147483647;
    int p = 2;
    printf("o*p=%d, %d\n", o*p, tmult_ok(o, p));
    printf("o*p=%d, %d\n", o*p, tmult_ok_v2(o, p));

    return 0;
}


int uadd_ok(unsigned x, unsigned y) {
    unsigned sum = x + y;
    return sum >= x;
}


int tadd_ok(int x, int y) {
    int sum = x + y;
    int neg_over = (x < 0 && y < 0 && sum >=0);
    int pos_over = (x >= 0 && y >= 0 && sum < 0);
    return !(neg_over || pos_over);
}


int tsub_ok(int x, int y) {
    if (x < 0 && y == -2147483648)
        return 1;
    else if (x >= 0 && y == -2147483648)
        return 0;
    else
        return tadd_ok(x, -y);
}


/* Determine whether arguments can be multiplied without overflow */
int tmult_ok(int x, int y) {
    int p = x * y;
    /* Either x is zero, or dividing p by x gives y */
    return !x || p/x == y;
}


/* Determine whether the arguments can be multiplied without overflow */
int tmult_ok_v2(int x, int y) {
    /* Compute product without overflow */
    int64_t pll = (int64_t) x * y;
    /* See if casting to int preserves value */
    return pll == (int) pll;
}

