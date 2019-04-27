#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    /*
    int fahr, celsius;
    int lower, upper, step;
    */
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;          /* 温度下限 */
    upper = 300;        /* 温度上限 */
    step = 20;          /* 增长步长 */

    printf("fahr => celsius\n");
    fahr = lower;
    while (fahr <= upper) {
        celsius = 5.0 * (fahr - 32.0) / 9.0;
        //printf("%3d  %6d\n", fahr, celsius);
        printf("%3.0f   %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }

    return 0;
}
