#include <stdio.h>


int is_equal(x, y) {
    return !(x^y);
}


int main()
{
    printf("-- 2.12 ---------------------\n");
    int m = 0x87654321;
    int m1 = m & 0xFF;
    int m2 = m ^ ~0xFF;
    int m3 = m | 0xFF;
    printf("m的最低有效位: %x\n", m1);
    printf("除了m的最低有效位, 其他位都取补: %x\n", m2);
    printf("m的最低有效字节设置成1, 其他字节不变: %x\n", m3);

    printf("-- 2.14 ---------------------\n");
    char x = 0x66;
    char y = 0x39;
    unsigned char z = ~x | ~y;
    printf("x & y = %.2x\n", x & y);
    printf("x | y = %.2x\n", x | y);
    printf("~x | ~y = %.2x\n", z);
    printf("x & !y = %.2x\n", x & !y);
    printf("x && y = %.2x\n", x && y);
    printf("x || y = %.2x\n", x || y);
    printf("!x||!y = %.2x\n", !x||!y);
    printf("x && ~y = %.2x\n", x && ~y);

    printf("-- 2.15 ---------------------\n");
    int a = 2;
    int b = 2;
    printf("is_equal(a, b)? %d\n", is_equal(a, b));
}
