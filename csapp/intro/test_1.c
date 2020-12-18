#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>


int main() {
    int lval = 0xFEDCBA98 << 0;
    int aval = 0xFEDCBA98 >> 4;
    unsigned int uval = 0xFEDCBA98 >> 8;
    printf("lval = %x\n", lval);
    printf("aval = %x\n", aval);
    printf("uval = %x\n", uval);

    int m = (1 << 2) + (3 << 4);
    printf("m = %x\n", m);

    char a = 0xC3;
    char b = a << 3;
    printf("a<<3=%x\n", b);
    printf("a>>2=%x\n", a>>2);

    int32_t x = 1;
    uint64_t y = 1;

    printf("x = %" PRId32 ", y = %" PRIu64 "\n", x, y);
    printf("sizeof(x) = %lu, sizeof(y) = %lu\n", sizeof(x), sizeof(y));

    return 0;
}
